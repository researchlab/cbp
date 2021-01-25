package main

import (
	"context"
	"io"
	"log"

	"google.golang.org/grpc"

	pb "github.com/researchlab/rpc-notes/grpc/basic/customer"
)

// createCustomer calls the RPC method CreateCustomer of CustomerServer
func createCustomer(client pb.CustomerClient, customer *pb.CustomerRequest) {
	resp, err := client.CreateCustomer(context.Background(), customer)
	if err != nil {
		log.Fatalf("could not create customer: %v", err)
	}
	if resp.Success {
		log.Printf("A new Customer has been added with id: %v", resp.Id)
	}
}

// getCustomers calls the RPC method GetCustomers of CustomerServer

func getCustomers(client pb.CustomerClient, filter *pb.CustomerFilter) {
	//calling the streaming API
	stream, err := client.GetCustomers(context.Background(), filter)
	if err != nil {
		log.Fatalf("Error on get customers: %v\n", err)
	}

	for {
		customer, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalf("%v.GetCustomers(_) = _, %v\n", client, err)
		}
		log.Printf("Customer: %v\n", customer)
	}
}

func main() {
	// Set up a connection to the gRPC server.
	conn, err := grpc.Dial("localhost:1234", grpc.WithInsecure())
	if err != nil {
		panic(err)
	}
	defer conn.Close()

	// creates a new customerClient
	client := pb.NewCustomerClient(conn)
	customerone := NewCustomerOne()
	customertwo := NewCustomerTwo()

	createCustomer(client, customerone)
	createCustomer(client, customertwo)

	//filter with an empty keyword
	filter := &pb.CustomerFilter{Keyword: ""}
	getCustomers(client, filter)
}

func NewCustomerOne() *pb.CustomerRequest {
	return &pb.CustomerRequest{
		Id:    101,
		Name:  "Shiju Varghese",
		Email: "shiju@xyz.com",
		Phone: "732-757-2923",
		Addresses: []*pb.CustomerRequest_Address{
			&pb.CustomerRequest_Address{
				Street:            "1 Mission Street",
				City:              "San Francisco",
				State:             "CA",
				Zip:               "94105",
				IsShippingAddress: false,
			},
			&pb.CustomerRequest_Address{
				Street:            "Greenfield",
				City:              "Kochi",
				State:             "KL",
				Zip:               "68356",
				IsShippingAddress: true,
			},
		},
	}
}

func NewCustomerTwo() *pb.CustomerRequest {
	return &pb.CustomerRequest{
		Id:    102,
		Name:  "Irene Rose",
		Email: "irene@xyz.com",
		Phone: "732-757-2924",
		Addresses: []*pb.CustomerRequest_Address{
			&pb.CustomerRequest_Address{
				Street:            "1 Mission Street",
				City:              "San Francisco",
				State:             "CA",
				Zip:               "94105",
				IsShippingAddress: true,
			},
		},
	}
}
