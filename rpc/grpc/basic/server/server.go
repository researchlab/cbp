package main

import (
	"context"
	"net"
	"strings"

	"google.golang.org/grpc"

	"github.com/researchlab/rpc-notes/grpc/basic/customer"
)

// server is used to implement customer.CustomerServer
type server struct {
	savedCustomers []*customer.CustomerRequest
}

// CreateCustomer creates a new Customer

func (s *server) CreateCustomer(ctx context.Context, in *customer.CustomerRequest) (*customer.CustomerResponse, error) {
	s.savedCustomers = append(s.savedCustomers, in)
	return &customer.CustomerResponse{Id: in.Id, Success: true}, nil
}

// GetCustomers returns all customers by given filter
func (s *server) GetCustomers(filter *customer.CustomerFilter, stream customer.Customer_GetCustomersServer) error {
	for _, ctm := range s.savedCustomers {
		if filter.Keyword != "" {
			if !strings.Contains(ctm.Name, filter.Keyword) {
				continue
			}
		}
		if err := stream.Send(ctm); err != nil {
			return err
		}
	}
	return nil
}

func main() {
	lis, err := net.Listen("tcp", ":1234")
	if err != nil {
		panic(err)
	}
	//create a new grpc server
	s := grpc.NewServer()
	customer.RegisterCustomerServer(s, &server{})
	s.Serve(lis)
}
