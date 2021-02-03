package server

import (
	"io"

	. "github.com/researchlab/cbp/rpc/binary/rpc"

	"go.uber.org/zap"
)

func (h *RPCHandler) processSetupTaskRequest(buf []byte) (*SetupTaskResponse, error) {
	req := &SetupTaskRequest{}
	err := req.Unmarshal(buf)
	if err != nil {
		return nil, err
	}

	h.Logger.Info("SetupTaskRequest received", zap.String("TaskID", req.TaskID))
	h.Logger.Info("SetupTaskRequest received", zap.Any("request body", req))

	resp := &SetupTaskResponse{
		ErrCode: 0,
		ErrMsg:  "support for test",
	}
	return resp, nil
}

func (h *RPCHandler) writeSetupTaskResponse(w io.Writer, resp *SetupTaskResponse, e error) {
	if resp == nil {
		resp = &SetupTaskResponse{}
	}

	if e != nil {
		resp.ErrCode = 1
		resp.ErrMsg = e.Error()
		h.Logger.Info("SetupTaskResponse err", zap.Error(e))
	} else if resp.ErrCode != 0 {
		h.Logger.Info("SetupTaskResponse err", zap.String("errmsg", resp.ErrMsg))
	} else {
		resp.ErrCode = 0
	}

	buf, err := resp.Marshal()
	if err != nil {
		h.Logger.Info("error marshalling setup task tran response", zap.Error(err))
		return
	}

	if err := WriteTLV(w, TypeSetupTaskResponse, buf); err != nil {
		h.Logger.Info("write setup task  response error", zap.Error(err))
		return
	}
}

func (h *RPCHandler) processRemoveTaskRequest(buf []byte) (*RemoveTaskResponse, error) {
	req := &RemoveTaskRequest{}
	err := req.Unmarshal(buf)
	if err != nil {
		return nil, err
	}
	h.Logger.Info("RemoveTaskReqeust received", zap.String("TaskID", req.TaskID))

	resp := &RemoveTaskResponse{
		ErrCode: 0,
		ErrMsg:  "RemoveTask support for test",
	}

	return resp, nil
}

func (h *RPCHandler) writeRemoveTaskResponse(w io.Writer, resp *RemoveTaskResponse, e error) {
	if resp == nil {
		resp = &RemoveTaskResponse{}
	}

	if e != nil {
		resp.ErrCode = 1
		resp.ErrMsg = e.Error()
		h.Logger.Info("RemoveTaskResponse err", zap.Error(e))
	} else if resp.ErrCode != 0 {
		h.Logger.Info("RemoveTaskResponse err", zap.String("errmsg", resp.ErrMsg))
	} else {
		resp.ErrCode = 0
	}

	buf, err := resp.Marshal()
	if err != nil {
		h.Logger.Info("error marshalling remove task response", zap.Error(err))
		return
	}

	if err := WriteTLV(w, TypeRemoveTaskResponse, buf); err != nil {
		h.Logger.Info("write remove task response error", zap.Error(err))
		return
	}
}
