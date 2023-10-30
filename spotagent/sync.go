package spotagent

import (
	"fmt"
	"sync/atomic"

	flatbuffers "github.com/google/flatbuffers/go"
	"github.com/thrasher-corp/gocryptotrader/exchanges/ticker"
	"github.com/thrasher-corp/gocryptotrader/hikyuu/flat"
	"go.nanomsg.org/mangos/v3"
	"go.nanomsg.org/mangos/v3/protocol/pub"
	_ "go.nanomsg.org/mangos/v3/transport/all"
)

const url = "ipc:///tmp/hikyuu_real_pub.ipc"

// const url = "tcp://127.0.0.1:40899"

var spotTopic = []byte(":spot:")
var startSpotTopic = []byte(":spot:[start spot]")

type Trans struct {
	socket    mangos.Socket
	sendCount atomic.Int64
}

func (s *Trans) CreateSocket() error {
	var err error
	sock, err := pub.NewSocket()
	if err != nil {
		return err
	}
	err = sock.Listen(url)
	if err != nil {
		return err
	}
	s.socket = sock
	return nil
}

func (s *Trans) send(data []byte) error {
	tmp := make([]byte, len(spotTopic)+len(data))
	copy(tmp, spotTopic)
	copy(tmp[len(spotTopic):], data)
	return s.socket.Send(tmp)
}
func (s *Trans) sendStart() error {
	return s.socket.Send(startSpotTopic)
}

func (s *Trans) Handle(service string, data interface{}) error {
	s.sendCount.Add(1)
	switch d := data.(type) {
	case *ticker.Price:
		fmt.Println(d.LastUpdated)
		builder := flatbuffers.NewBuilder(1024)

		// strings must be created before the start of the table they are referenced in
		market := builder.CreateString("OKX")
		code := builder.CreateString(d.Pair.String())
		name := builder.CreateString(d.Pair.String())
		dt := builder.CreateString(d.LastUpdated.Format("2006-01-02 15:04:05.000"))
		flat.SpotStart(builder)
		flat.SpotAddMarket(builder, market)
		flat.SpotAddCode(builder, code)
		flat.SpotAddName(builder, name)
		flat.SpotAddDatetime(builder, dt)
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
		if s.sendCount.Load()%100 == 0 {
			s.sendStart()
		}
		err := s.send(buf)
		if err != nil {
			return err
		}
	}
	return nil
}
