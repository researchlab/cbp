package client

import (
	"errors"
	"net"

	. "github.com/researchlab/cbp/rpc/binary/rpc"
)

func CallSetupTaskRequest(addr string, taskID string, hostOsType string, hostOsName string) (*SetupTaskResponse, error) {
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		return nil, err
	}
	defer conn.Close()

	req := &SetupTaskRequest{}
	req.TaskID = taskID
	req.HostOsType = hostOsType
	req.HostOsName = hostOsName

	buf, err := req.Marshal()
	if err != nil {
		return nil, err
	}
	if err := WriteTLV(conn, TypeSetupTaskRequest, buf); err != nil {
		return nil, err
	}

	typ, err := ReadType(conn)
	if err != nil {
		return nil, err
	}
	if typ != TypeSetupTaskResponse {
		return nil, errors.New("setup task trans resp type not match")
	}
	//type == write
	buf, err = ReadLV(conn)
	if err != nil {
		return nil, err
	}
	trans := &SetupTaskResponse{}
	err = trans.Unmarshal(buf)

	return trans, err
}

func CallRemoveTaskRequest(addr string, req *RemoveTaskRequest) (*RemoveTaskResponse, error) {
	conn, err := net.Dial("tcp", addr)
	if err != nil {
		return nil, err
	}
	defer conn.Close()

	buf, err := req.Marshal()
	if err != nil {
		return nil, err
	}
	if err := WriteTLV(conn, TypeRemoveTaskRequest, buf); err != nil {
		return nil, err
	}

	typ, err := ReadType(conn)
	if err != nil {
		return nil, err
	}
	if typ != TypeRemoveTaskResponse {
		return nil, errors.New("remove task trans resp type not match")
	}
	//type == write
	buf, err = ReadLV(conn)
	if err != nil {
		return nil, err
	}
	trans := &RemoveTaskResponse{}
	err = trans.Unmarshal(buf)

	return trans, err
}
