package main

import "fmt"
import "math"

// https://tour.golang.org/methods/1

type Vertex struct {
    X, Y float64
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    v := Vertex{3, 4}
    fmt.Printf("%s\n",v)
    fmt.Printf("%s\n",v.Abs())
    fmt.Printf("%s\n",v.Abs())
}
