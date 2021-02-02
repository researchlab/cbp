package rpc

import (
	"github.com/gogo/protobuf/proto"
	"github.com/researchlab/cbp/rpc/binary/rpc/meta"
)

type RemoveTaskRequest struct {
	TaskID   string
	UserName string
	Passwd   string
}

type RemoveTaskResponse struct {
	ErrCode int32
	ErrMsg  string
}

func (trans *RemoveTaskRequest) Marshal() ([]byte, error) {
	pb := &meta.RemoveTaskRequest{}
	pb.TaskID = &trans.TaskID
	pb.UserName = &trans.UserName
	pb.Passwd = &trans.Passwd

	return proto.Marshal(pb)
}

func (trans *RemoveTaskRequest) Unmarshal(buf []byte) error {
	var pb meta.RemoveTaskRequest
	if err := proto.Unmarshal(buf, &pb); err != nil {
		return err
	}

	trans.TaskID = pb.GetTaskID()
	trans.UserName = pb.GetUserName()
	trans.Passwd = pb.GetPasswd()

	return nil
}

func (trans *RemoveTaskResponse) Marshal() ([]byte, error) {
	pb := &meta.RemoveTaskResponse{}

	pb.ErrCode = &trans.ErrCode
	pb.ErrMsg = &trans.ErrMsg

	return proto.Marshal(pb)
}

func (trans *RemoveTaskResponse) Unmarshal(buf []byte) error {
	var pb meta.RemoveTaskResponse
	if err := proto.Unmarshal(buf, &pb); err != nil {
		return err
	}

	trans.ErrCode = pb.GetErrCode()
	trans.ErrMsg = pb.GetErrMsg()

	return nil
}

type SetupTaskRequest struct {
	TaskID     string
	HostOsType string
	HostOsName string
}

func (trans *SetupTaskRequest) Marshal() ([]byte, error) {
	pb := &meta.SetupTaskRequest{}
	pb.TaskID = &trans.TaskID
	pb.HostOsType = &trans.HostOsType
	pb.HostOsName = &trans.HostOsName

	return proto.Marshal(pb)
}

func (trans *SetupTaskRequest) Unmarshal(buf []byte) error {
	var pb meta.SetupTaskRequest
	if err := proto.Unmarshal(buf, &pb); err != nil {
		return err
	}
	trans.TaskID = pb.GetTaskID()
	trans.HostOsType = pb.GetHostOsType()
	trans.HostOsName = pb.GetHostOsName()

	return nil
}

type SetupTaskResponse struct {
	ErrCode int32
	ErrMsg  string
}

func (trans *SetupTaskResponse) Marshal() ([]byte, error) {
	pb := &meta.SetupTaskResponse{}
	pb.ErrCode = &trans.ErrCode
	pb.ErrMsg = &trans.ErrMsg
	return proto.Marshal(pb)
}

func (trans *SetupTaskResponse) Unmarshal(buf []byte) error {
	var pb meta.SetupTaskResponse
	if err := proto.Unmarshal(buf, &pb); err != nil {
		return err
	}
	trans.ErrCode = pb.GetErrCode()
	trans.ErrMsg = pb.GetErrMsg()

	return nil
}
