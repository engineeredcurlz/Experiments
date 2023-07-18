package main

import "fmt"
// variables x,y  will be the assigned string, with output being the string
func swap (x, y string) (string, string) {
	return y, x // return the variables
}

func main() {
	a, b := swap ("hello", "world")
	fmt.Println(a, b)
}

// swap returns two strings