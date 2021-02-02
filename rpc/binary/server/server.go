package server

import (
	"net"

	"go.uber.org/zap"
)

// Server processes data received over raw TCP connections.
type Server struct {
	RPCHandler *RPCHandler
	addr       string
	rpcPort    string
	err        chan error

	Logger *zap.Logger
}

// WithLogger sets the logger on the service.
func (s *Server) WithLogger(log *zap.Logger) {
	s.Logger = log.With(zap.String("service", "transport"))
	s.RPCHandler.Logger = s.Logger
}

// NewServer returns a new instance of Server.
func NewServer() *Server {
	s := &Server{
		addr:       "0.0.0.0",
		rpcPort:    "8089",
		err:        make(chan error),
		Logger:     zap.NewNop(),
		RPCHandler: newRPCHandler(),
	}

	return s
}

// Open starts the service
func (s *Server) Open() error {
	s.Logger.Info("Starting cmigrate transport service")

	// Open listener.
	var err error
	s.RPCHandler.Ln, err = net.Listen("tcp", s.addr+":"+s.rpcPort)
	if err != nil {
		return err
	}

	s.Logger.Info("Listening on RPC TCP:",
		zap.Stringer("addr", s.RPCHandler.Ln.Addr()))

	go s.RPCHandler.serve()

	return nil
}

// Close closes the underlying listener.
func (s *Server) Close() error {
	s.RPCHandler.Close()

	return nil
}

// Err returns a channel for fatal errors that occur on the listener.
func (s *Server) Err() <-chan error { return s.err }
