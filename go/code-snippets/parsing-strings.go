package main

// https://golang.org/pkg/strconv/

import "fmt"
import "strconv"


func main() {
    // https://golang.org/pkg/strconv/
    fmt.Println("hello world")
    b, err := strconv.ParseBool("true")
    fmt.Printf(" %s \n %s \n", b, err)

    b, err = strconv.ParseBool("truee")
    fmt.Printf(" %s \n %s \n", b, err)
}
