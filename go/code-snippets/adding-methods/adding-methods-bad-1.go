package main
// https://golang.org/pkg/strconv/

// This fails ... because we are trying to add a method to a type that was not
// defined in this class (float64)
func (v float64) Abs() float64 {
    return 1.1
}

func main() {
}
