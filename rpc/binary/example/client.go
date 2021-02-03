package main

import (
	"fmt"

	. "github.com/researchlab/cbp/rpc/binary/client"
	. "github.com/researchlab/cbp/rpc/binary/rpc"
)

func main() {

	//do test
	trans, err := CallSetupTaskRequest("127.0.0.1:8089", "taskid000", "linux", "3.10.0.el7.x86_64")
	if err != nil {
		fmt.Errorf("call get trans info failed: %s\n", err.Error())
		return
	}

	fmt.Println(trans)

	req := &RemoveTaskRequest{}
	req.TaskID = "taskid000"

	t, err := CallRemoveTaskRequest("127.0.0.1:8089", req)
	if err != nil {
		fmt.Errorf("call remove trans task failed: %s\n", err.Error())
		return
	}

	fmt.Println(t)
}
