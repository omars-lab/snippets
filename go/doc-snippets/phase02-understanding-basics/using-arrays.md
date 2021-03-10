# Growing Lists ...
https://www.openmymind.net/Controlling-Array-Growth-In-Golang/

https://tour.golang.org/moretypes/13

```
package main

import "fmt"

func main() {
	a := make([]int, 5)
	printSlice("a", a)
	a[5] = 5
	a[6] = 6

	b := make([]int, 0, 5)
	printSlice("b", b)
	// b[5] = 5
	// b[6] = 6

	c := b[:2]
	printSlice("c", c)

	d := c[2:5]
	printSlice("d", d)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n", s, len(x), cap(x), x)
}
```

# Mapping Elements in List
https://stackoverflow.com/questions/33726731/short-way-to-apply-a-function-to-all-elements-in-a-list-in-golang
