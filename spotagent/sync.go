package spotagent

import (
	"fmt"

	flatbuffers "github.com/google/flatbuffers/go"
	"github.com/thrasher-corp/gocryptotrader/exchanges/ticker"
	"github.com/thrasher-corp/gocryptotrader/hikyuu/flat"
	"go.nanomsg.org/mangos/v3"
	"go.nanomsg.org/mangos/v3/protocol/req"
	_ "go.nanomsg.org/mangos/v3/transport/ipc"
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
	err = sock.Listen("ipc:///tmp/hikyuu_real_pub.ipc")
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

		// strings must be created before the start of the table they are referenced in
		market := builder.CreateString("OKX")
		code := builder.CreateString(d.Pair.String())
		name := builder.CreateString(d.Pair.String())
		dt := builder.CreateString(d.LastUpdated.String())
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
		err := s.send(buf)
		if err != nil {
			return err
		}
	}
	return nil
}
