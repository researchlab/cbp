package main

import (
	"bytes"
	"log"
	"net/http"

	"github.com/gorilla/rpc/json"
	"github.com/researchlab/rpc-notes/jsonrpc/v2/arith"
)

func main() {
	url := "http://localhost:1234/rpc"
	args := arith.Args{2, 3}
	msg, err := json.EncodeClientRequest("Arith.Multiply", args)
	if err != nil {
		log.Fatalf("%s\n", err)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(msg))
	if err != nil {
		log.Fatalf("%s\n", err)
	}
	req.Header.Set("Content-Type", "application/json")
	client := new(http.Client)
	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Error in sending request to %s. %s", url, err)
	}
	defer resp.Body.Close()

	var result arith.Result
	err = json.DecodeClientResponse(resp.Body, &result)
	if err != nil {
		log.Fatalf("Couldn't decode response. %s", err)
	}
	log.Printf("%d*%d=%d\n", args.A, args.B, result)
}
