package main

import (
	"log"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"

	"github.com/researchlab/rpc-notes/jsonrpc/service"
)

func init() {
	//rpc.Register(service.CalcService{})
	rpc.RegisterName("Calc", service.CalcService{})
}

func main() {
	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		panic(err)
	}
	log.Printf("rpcserver start by port %v\n", ":1234")
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("accept error: %v\n", err)
			continue
		}

		go jsonrpc.ServeConn(conn)
	}
}
