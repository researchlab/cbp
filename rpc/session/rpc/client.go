package rpc

import "net"

type Client struct {
	conn net.Conn
}

func NewClient(conn net.Conn) *Client {
	return &Client{conn: conn}
}

// client.RpcCall("login", &req)
func (c *Client) RpcCall(name string, fpr interface{}) {

}
