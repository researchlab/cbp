package server

import (
	"net"
	"strings"
	"sync"

	. "github.com/researchlab/cbp/rpc/binary/rpc"
	"go.uber.org/zap"
)

var PredictDoneTimeCalculatePeriod = int64(10)

type RPCHandler struct {
	wg     sync.WaitGroup
	Done   chan struct{}
	Ln     net.Listener
	Logger *zap.Logger
}

func newRPCHandler() *RPCHandler {
	return &RPCHandler{
		Done: make(chan struct{}),
	}
}

func (h *RPCHandler) Close() {
	if h.Done != nil {
		close(h.Done)
		h.wg.Wait()
	}
}

func (h *RPCHandler) serve() {
	h.wg.Add(1)
	defer h.wg.Done()

	for {
		// Check if the service is shutting down.
		select {
		case <-h.Done:
			return
		default:
		}

		// Accept the next connection.
		conn, err := h.Ln.Accept()
		if err != nil {
			if strings.Contains(err.Error(), "connection closed") {
				h.Logger.Error("cluster service accept error", zap.Error(err))
				return
			}
			h.Logger.Error("accept error", zap.Error(err))
			continue
		}

		// Delegate connection handling to a separate goroutine.
		h.wg.Add(1)
		go func() {
			defer h.wg.Done()
			h.handleConn(conn)
		}()
	}
}

// handleConn services an individual TCP connection.
func (h *RPCHandler) handleConn(conn net.Conn) {
	// Ensure connection is closed when service is closed.
	closing := make(chan struct{})
	defer close(closing)
	go func() {
		select {
		case <-closing:
		case <-h.Done:
		}
		conn.Close()
	}()

	h.Logger.Debug("accept remote connection", zap.String("remoteaddr", conn.RemoteAddr().String()))
	defer func() {
		h.Logger.Debug("close remote connection", zap.String("remoteaddr", conn.RemoteAddr().String()))
	}()
	for {
		// Read type-length-value.
		typ, err := ReadType(conn)
		if err != nil {
			if strings.HasSuffix(err.Error(), "EOF") {
				return
			}
			h.Logger.Info("unable to read type", zap.Error(err))
			return
		}

		// Delegate message processing by type.
		switch typ {
		case TypeSetupTaskRequest:
			buf, err := ReadLV(conn)
			if err != nil {
				h.Logger.Error("unable to read length-value", zap.Error(err))
				return
			}

			resp, err := h.processSetupTaskRequest(buf)
			if err != nil {
				h.Logger.Error("process setup task transport error", zap.Error(err))
			}
			h.writeSetupTaskResponse(conn, resp, err)
		case TypeRemoveTaskRequest:
			buf, err := ReadLV(conn)
			if err != nil {
				h.Logger.Error("unable to read length-value", zap.Error(err))
				return
			}

			resp, err := h.processRemoveTaskRequest(buf)
			if err != nil {
				h.Logger.Info("process remove task error", zap.Error(err))
			}
			h.writeRemoveTaskResponse(conn, resp, err)
		default:
			h.Logger.Info("transport service message type not found", zap.Binary("type", []byte{typ}))
		}

		return
	}
}
