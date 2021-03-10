package main
// https://golang.org/pkg/strconv/

import "fmt"

type MyFloat float64

func (v MyFloat) Abs() float64 {
    return 1.1
}

func main() {
    var f MyFloat
    fmt.Println(f.Abs())
}
