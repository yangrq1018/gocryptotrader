package atr

import (
	"fmt"
	"time"

	"github.com/shopspring/decimal"
	"github.com/thrasher-corp/gct-ta/indicators"
	"github.com/thrasher-corp/gocryptotrader/backtester/common"
	"github.com/thrasher-corp/gocryptotrader/backtester/data"
	"github.com/thrasher-corp/gocryptotrader/backtester/eventhandlers/portfolio"
	"github.com/thrasher-corp/gocryptotrader/backtester/eventhandlers/strategies/base"
	"github.com/thrasher-corp/gocryptotrader/backtester/eventtypes/signal"
	"github.com/thrasher-corp/gocryptotrader/backtester/funding"
	gctcommon "github.com/thrasher-corp/gocryptotrader/common"
	"github.com/thrasher-corp/gocryptotrader/exchanges/order"
)

const (
	// Name is the strategy name
	Name                  = "atr"
	atrPeriodKey          = "atr-period"
	centralTrackPeriodKey = "central-track-period"
	trackMultiplierKey    = "track-multiplier"
	description           = `The relative strength index is a technical indicator used in the analysis of financial markets. It is intended to chart the current and historical strength or weakness of a stock or market based on the closing prices of a recent trading period`
)

// Strategy is an implementation of the Handler interface
type Strategy struct {
	base.Strategy
	atrPeriod          decimal.Decimal
	centralTrackPeriod decimal.Decimal
	trackMultiplier    decimal.Decimal
}

// Name returns the name of the strategy
func (s *Strategy) Name() string {
	return Name
}

// Description provides a nice overview of the strategy
// be it definition of terms or to highlight its purpose
func (s *Strategy) Description() string {
	return description
}

// OnSignal handles a data event and returns what action the strategy believes should occur
// For rsi, this means returning a buy signal when rsi is at or below a certain level, and a
// sell signal when it is at or above a certain level
func (s *Strategy) OnSignal(d data.Handler, _ funding.IFundingTransferer, _ portfolio.Handler) (signal.Event, error) {
	if d == nil {
		return nil, common.ErrNilEvent
	}
	es, err := s.GetBaseData(d)
	if err != nil {
		return nil, err
	}

	latest, err := d.Latest()
	if err != nil {
		return nil, err
	}

	es.SetPrice(latest.GetClosePrice())

	if offset := latest.GetOffset(); offset <= s.atrPeriod.IntPart() {
		es.AppendReason("Not enough data for signal generation")
		es.SetDirection(order.DoNothing)
		return &es, nil
	}

	dataRangeHigh, err := d.StreamHigh()
	if err != nil {
		return nil, err
	}
	dataRangeLow, err := d.StreamLow()
	if err != nil {
		return nil, err
	}
	dataRangeClose, err := d.StreamClose()
	if err != nil {
		return nil, err
	}
	var massagedDataHigh, massagedDataLow, massagedDataClose []float64
	massagedDataHigh, err = s.massageMissingData(dataRangeHigh, es.GetTime())
	if err != nil {
		return nil, err
	}
	massagedDataLow, err = s.massageMissingData(dataRangeLow, es.GetTime())
	if err != nil {
		return nil, err
	}
	massagedDataClose, err = s.massageMissingData(dataRangeClose, es.GetTime())
	if err != nil {
		return nil, err
	}

	atr := indicators.ATR(massagedDataHigh, massagedDataLow, massagedDataClose, int(s.atrPeriod.IntPart()))
	latestATRValue := decimal.NewFromFloat(atr[len(atr)-1])
	hasDataAtTime, err := d.HasDataAtTime(latest.GetTime())
	if err != nil {
		return nil, err
	}
	if !hasDataAtTime {
		es.SetDirection(order.MissingData)
		es.AppendReasonf("missing data at %v, cannot perform any actions. ATR %v", latest.GetTime(), latestATRValue)
		return &es, nil
	}

	centralTrack := indicators.MA(massagedDataClose, int(s.centralTrackPeriod.IntPart()), indicators.Sma)
	latestCentralTrack := decimal.NewFromFloat(centralTrack[len(centralTrack)-1])
	latestClose := decimal.NewFromFloat(massagedDataClose[len(massagedDataClose)-1])
	upperTrack := latestCentralTrack.Add(s.trackMultiplier.Mul(latestATRValue))
	lowerTrack := latestCentralTrack.Sub(s.trackMultiplier.Mul(latestATRValue))
	switch {
	case latestClose.GreaterThanOrEqual(upperTrack):
		es.SetDirection(order.Buy)
	case latestClose.LessThanOrEqual(lowerTrack):
		es.SetDirection(order.Sell)
	default:
		es.SetDirection(order.DoNothing)
	}
	es.AppendReasonf("ATR at %v, lower %v, upper %v, current %v",
		latestATRValue, lowerTrack, upperTrack, latestClose)

	return &es, nil
}

// SupportsSimultaneousProcessing highlights whether the strategy can handle multiple currency calculation
// There is nothing actually stopping this strategy from considering multiple currencies at once
// but for demonstration purposes, this strategy does not
func (s *Strategy) SupportsSimultaneousProcessing() bool {
	return true
}

// OnSimultaneousSignals analyses multiple data points simultaneously, allowing flexibility
// in allowing a strategy to only place an order for X currency if Y currency's price is Z
func (s *Strategy) OnSimultaneousSignals(d []data.Handler, _ funding.IFundingTransferer, _ portfolio.Handler) ([]signal.Event, error) {
	var resp []signal.Event
	var errs error
	for i := range d {
		latest, err := d[i].Latest()
		if err != nil {
			return nil, err
		}
		sigEvent, err := s.OnSignal(d[i], nil, nil)
		if err != nil {
			errs = gctcommon.AppendError(errs, fmt.Errorf("%v %v %v %w",
				latest.GetExchange(),
				latest.GetAssetType(),
				latest.Pair(),
				err))
		} else {
			resp = append(resp, sigEvent)
		}
	}
	return resp, errs
}

// SetCustomSettings allows a user to modify the RSI limits in their config
func (s *Strategy) SetCustomSettings(customSettings map[string]interface{}) error {
	for k, v := range customSettings {
		switch k {
		case atrPeriodKey:
			atrPeriod, ok := v.(float64)
			if !ok || atrPeriod <= 0 {
				return fmt.Errorf("%w provided atr-period value could not be parsed: %v", base.ErrInvalidCustomSettings, v)
			}
			s.atrPeriod = decimal.NewFromFloat(atrPeriod)
		case centralTrackPeriodKey:
			centralTrackPeriod, ok := v.(float64)
			if !ok || centralTrackPeriod <= 0 {
				return fmt.Errorf("%w provided central-track-period value could not be parsed: %v", base.ErrInvalidCustomSettings, v)
			}
			s.centralTrackPeriod = decimal.NewFromFloat(centralTrackPeriod)
		case trackMultiplierKey:
			trackMultiplier, ok := v.(float64)
			if !ok || trackMultiplier <= 0 {
				return fmt.Errorf("%w provided track-multiplier value could not be parsed: %v", base.ErrInvalidCustomSettings, v)
			}
			s.trackMultiplier = decimal.NewFromFloat(trackMultiplier)
		default:
			return fmt.Errorf("%w unrecognised custom setting key %v with value %v. Cannot apply", base.ErrInvalidCustomSettings, k, v)
		}
	}

	return nil
}

// SetDefaults sets the custom settings to their default values
func (s *Strategy) SetDefaults() {
	s.atrPeriod = decimal.NewFromInt(14)
	s.centralTrackPeriod = decimal.NewFromInt(24)
	s.trackMultiplier = decimal.NewFromFloat(1.0)
}

// massageMissingData will replace missing data with the previous candle's data
// this will ensure that RSI can be calculated correctly
// the decision to handle missing data occurs at the strategy level, not all strategies
// may wish to modify data
func (s *Strategy) massageMissingData(data []decimal.Decimal, t time.Time) ([]float64, error) {
	resp := make([]float64, len(data))
	var missingDataStreak int64
	for i := range data {
		if data[i].IsZero() && i > int(s.atrPeriod.IntPart()) {
			data[i] = data[i-1]
			missingDataStreak++
		} else {
			missingDataStreak = 0
		}
		if missingDataStreak >= s.atrPeriod.IntPart() {
			return nil, fmt.Errorf("missing data exceeds ATR period length of %v at %s and will distort results. %w",
				s.atrPeriod,
				t.Format(time.DateTime),
				base.ErrTooMuchBadData)
		}
		resp[i] = data[i].InexactFloat64()
	}
	return resp, nil
}
