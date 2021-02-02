package client

import (
	"testing"

	. "github.com/researchlab/cbp/rpc/binary/rpc"
)

func TestSetupTask(t *testing.T) {
	//do test
	trans, err := CallSetupTaskRequest("127.0.0.1:8089", "taskid000", "linux", "3.10.0.el7.x86_64")
	if err != nil {
		t.Errorf("call get trans info failed: %s\n", err.Error())
		return
	}

	if trans.ErrCode != 0 {
		t.Errorf("trans info ErrCode != 0 : %s\n", trans.ErrMsg)
	}
	t.Log(trans)
}

func TestRemoveTask(t *testing.T) {
	req := &RemoveTaskRequest{}
	req.TaskID = "taskid000"

	trans, err := CallRemoveTaskRequest("127.0.0.1:8089", req)
	if err != nil {
		t.Errorf("call remove trans task failed: %s\n", err.Error())
		return
	}

	if trans.ErrCode != 0 {
		t.Errorf("trans remove task ErrCode != 0 : %s\n", trans.ErrMsg)
	}
	t.Log(trans)
}
