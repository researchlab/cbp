package arith

import (
	"net/http"
)

type Args struct {
	A, B int
}

type Arith int

type Result int

func (t *Arith) Multiply(r *http.Request, args *Args, result *Result) error {
	*result = Result(args.A * args.B)
	return nil
}
