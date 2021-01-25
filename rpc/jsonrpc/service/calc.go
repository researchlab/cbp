package service

import "errors"

type CalcService struct{}

type Args struct {
	A, B int
}

func (CalcService) Div(args Args, result *float64) error {
	if args.B == 0 {
		return errors.New("division by zero")
	}

	*result = float64(args.A) / float64(args.B)

	return nil
}

func (CalcService) Sum(args Args, result *float64) error {
	*result = float64(args.A + args.B)
	return nil
}
