package main

import "math"

// https://tour.golang.org/methods/1
type Vertex struct {
    X, Y float64
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// This fails because we are trying to override the same method twice ...
func (v Vertex) Abs() float64 {
    return 1.1
}

func main() {
}
