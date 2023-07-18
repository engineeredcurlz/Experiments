package main

import "fmt"

func split(sum int) (x, y int) {
	x = sum * 4 / 9 // 17*4= 68, 68/9= 7.5, integers are whole numbers, in case of division - we round down. x = 7
	y = sum - x // 17-7 = 10
	return
}

func main() {
	fmt.Println(split(17)) // should return 7, 10
}

// using a return statement without args returns the named return value (split)
// also called a "naked" return
// best for short functions as this can make longer functions hard to read