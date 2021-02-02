package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/researchlab/cbp/rpc/binary/server"
)

func main() {
	s := server.NewServer()
	if err := s.Open(); err != nil {
		fmt.Errorf("open server: %s", err)
		return
	}
	logger, err := server.InitLogger()
	if err != nil {
		fmt.Errorf("init logger failed:%v", err)
		return
	}
	s.WithLogger(logger)
	// monitorServerErrors
	go func() {
		for {
			select {
			case err := <-s.Err():
				fmt.Errorf("server error: %s\n", err)
			}
		}
	}()

	signalCh := make(chan os.Signal, 1)
	signal.Notify(signalCh, os.Interrupt, syscall.SIGTERM)
	fmt.Println("Listening for signals")

	// Block until one of the signals above is received
	<-signalCh
	fmt.Println("Signal received, initializing clean shutdown...")
	closed := make(chan bool)
	go func() {
		if s != nil {
			s.Close()
		}
		closed <- true
	}()

	// Block again until another signal is received, a shutdown timeout elapses, or the command is gracefully closed
	fmt.Println("Waiting for clean shutdown...")
	select {
	case <-signalCh:
		fmt.Println("Second signal received, initializing hard shutdown")
	case <-time.After(time.Second * 30):
		fmt.Println("Time limit reached, initializing hard shutdown")
	case <-closed:
		close(closed)
		fmt.Println("Server shutdown completed")
	}
	return
}
