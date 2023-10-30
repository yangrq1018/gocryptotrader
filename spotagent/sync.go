package spotagent

import (
	"fmt"

	flatbuffers "github.com/google/flatbuffers/go"
	"github.com/thrasher-corp/gocryptotrader/exchanges/ticker"
	"github.com/thrasher-corp/gocryptotrader/hikyuu/flat"
	"nanomsg.org/go/mangos/v2"
	"nanomsg.org/go/mangos/v2/protocol/req"
)

type Trans struct {
	socket mangos.Socket
}

func (s *Trans) CreateSocket() error {
	var err error
	sock, err := req.NewSocket()
	if err != nil {
		return err
	}
	err = sock.Listen("ipc://hikyuu_real_pub.ipc")
	if err != nil {
		return err
	}
	s.socket = sock
	return nil
}

func (s *Trans) send(data []byte) error {
	return s.socket.Send(data)
}

func (s *Trans) Handle(service string, data interface{}) error {
	switch d := data.(type) {
	case *ticker.Price:
		fmt.Println(d.LastUpdated)
		builder := flatbuffers.NewBuilder(1024)

		flat.SpotStart(builder)
		flat.SpotAddMarket(builder, builder.CreateString("OKX"))
		flat.SpotAddCode(builder, builder.CreateString(d.Pair.String()))
		flat.SpotAddName(builder, builder.CreateString(d.Pair.String()))
		flat.SpotAddDatetime(builder, builder.CreateString(d.LastUpdated.String()))
		// flat.SpotAddYesterdayClose(builder, d.Close)
		flat.SpotAddOpen(builder, d.Open)
		flat.SpotAddHigh(builder, d.High)
		flat.SpotAddLow(builder, d.Low)
		flat.SpotAddClose(builder, d.Close)
		flat.SpotAddAmount(builder, d.Volume)
		flat.SpotAddVolume(builder, d.Volume)

		flat.SpotAddBid1(builder, d.Bid)
		flat.SpotAddBid1Amount(builder, d.BidSize)
		// other orderbook is not available

		flat.SpotAddAsk1(builder, d.Ask)
		flat.SpotAddAsk1Amount(builder, d.AskSize)
		// other orderbook is not available
		spot := flat.SpotEnd(builder)

		flat.SpotListStartSpotVector(builder, 1)
		builder.PrependUOffsetT(spot)
		list := builder.EndVector(1)

		flat.SpotListStart(builder)
		flat.SpotListAddSpot(builder, list)
		spotList := flat.SpotListEnd(builder)

		builder.Finish(spotList)

		buf := builder.FinishedBytes()
		err := s.send(buf)
		if err != nil {
			return err
		}
	}
	return nil
}
