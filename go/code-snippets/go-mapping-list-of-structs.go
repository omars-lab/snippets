package main

import "fmt"

type Vertex struct {
	x int
	y int
}

func main() {
	elems := []*Vertex{&Vertex{1,1}, &Vertex{2,2}}
	fmt.Println(elems)
	for _, e := range elems {
		fmt.Println(*e)
	}
	for i := range elems {
		v := elems[i]
		(*v).y = (*v).y * 2
		(*v).x = (*v).x * 2
		elems[i] = v
	}
	fmt.Println(elems)
	for _, e := range elems {
		fmt.Println(*e)
	}
}

