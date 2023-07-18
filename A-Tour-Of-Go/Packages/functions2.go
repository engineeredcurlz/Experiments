package main

import "fmt"

func add(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}

// two or more named consecutive functions type can be omitted except the very last one if they are shared