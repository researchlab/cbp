package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/gorilla/rpc"
	"github.com/gorilla/rpc/json"
	"github.com/researchlab/rpc-notes/jsonrpc/v2/arith"
)

func main() {
	s := rpc.NewServer()
	s.RegisterCodec(json.NewCodec(), "application/json")
	s.RegisterCodec(json.NewCodec(), "application/json;charset=UTF-8")
	a := new(arith.Arith)
	s.RegisterService(a, "")
	r := mux.NewRouter()
	r.Handle("/rpc", s)
	log.Printf("server start at port 1234")
	http.ListenAndServe(":1234", r)
}
