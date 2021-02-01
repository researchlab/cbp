package main

import (
	"fmt"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"

	"github.com/researchlab/cbp/rpc/jsonrpc/service"
)

func main() {
	conn, err := net.Dial("tcp", ":1234")
	if err != nil {
		panic(err)
	}

	client := jsonrpc.NewClient(conn)
	//demo1(client)
	demo2(client)
	demo3(client)
	demo4(client)
}

//asynchronous call
func demo3(client *rpc.Client) {
	var result float64
	divCall := client.Go("Calc.Div", service.Args{10, 2}, &result, nil)
	replyCall := <-divCall.Done
	fmt.Printf("Calc.Div res: %v, err: %v\n", result, replyCall.Error)
}

func demo4(client *rpc.Client) {
	var result float64
	call := make(chan *rpc.Call, 1)
	client.Go("Calc.Sum", service.Args{10, 2}, &result, call)
	callDone := <-call
	fmt.Printf("Calc.Sum res: %v, err: %v\n", result, callDone.Error)
}

// synchronous call
func demo2(client *rpc.Client) {
	var result float64
	err := client.Call("Calc.Div", service.Args{10, 2}, &result)
	fmt.Printf("Calc.Div res: %v, err: %v\n", result, err)

	err = client.Call("Calc.Sum", service.Args{10, 2}, &result)
	fmt.Printf("Calc.Sum res: %v, err: %v\n", result, err)
}

func demo1(client *rpc.Client) {
	var result float64
	err := client.Call("CalcService.Div", service.Args{10, 3}, &result)
	fmt.Printf("res: %v, err: %v\n", result, err)

	err = client.Call("CalcService.Div", service.Args{10, 0}, &result)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Printf("res: %v\n", result)

}
