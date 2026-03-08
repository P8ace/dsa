[GO by example](https://gobyexample.com/)
### Functions

variadic parameters
```Go
	func concat(str ...string) string()
```


### Error Interface:
An error is any type that implements the Error interface

```Go
type error interface
	Error() string
}

//Example implementation of the Error interface

type DivideError struct{
	dividend float64
}

func (d DivideError) Error() string{
    return fmt.Sprintf("Cannot divide %.2f with zero.",d.dividend)
}

func divide(dividend, divisor float64) (flot64, error) {
	if divisor == 0{
		return 0, DivideError{dividend: dividend}
	}
	return dividend/divisor, nil
}
```
[Erros package](https://pkg.go.dev/errors#New)

```Go
var err error = errors.New("something went wrong")

// or
if errors.is(err, DivideError){
	fmt.Println("Received a Divide Error.")
}

// Wrapped errors: %w wraps the error with additional context
if err != nil{
	return fmt.Errorf("Received an error %w", err)
}

// Unwrap method on the error type
func (d DivideError) Unwrap() error {
	return d.dividend
}
```

#### Panic and Recover

When a function calls panic, the program crashes and prints the stack trace.
The panic function removes the control out of the current function and up the stack trace until it reaches a 
defered recover() function. If there is no recover function in the stack, the program crashes.


### Loops

```Go
// for INITAL; CONDITION; AFTER {
// 
// }

for i:= 0; i <10; i++{
	fmt.Println(i)
}

//for INITIAL; ; AFTER{
// 
//}
// 

// for CONDITION {
// }

data = 10
for data > 5 {
	//do something
	data--
}

//or simply a forever loop 

for {
	//do something
	continue // stop the current iteration and continue the next iteration
	//do semething
	break // stop the current iteration and exit the loop
}
````

### Arrays & Slices

Arrays

```Go
	var a [10]int
	b := [5]int{1,2,3,4,5}
	c := [...]int{6,7,8,9,0}
```

Slices
Zero value of a slice is nil.

```Go
	var a []int
	s := make([]string,len:3,cap:10)

// slice literal
	b := []int{1,2,3,4,5}
	func myfunc(){
		printNumbers(b...)
	}
	
// string to a slice
	data := []rune(word) //word is a string, being converted to a slice of runes(int32)
```

#### Range function
 for INDEX, ELEMENT := range SLICE {
    // do something
 }
 

### Maps
Zero value of a map is nil

```Go
	myMap := make(map[int]string)
	myMap[20] = "John"
	myMap[30] = "jane"
	
// Map literal
	myMap2 = map[int]string{
		40: "William",
		50: "George",
	}

	len(myMap2) //2
	
// Mutations
	m[key] = value
	
// Get an element
	elem := m[key]
	
// Delete an element
	delete(m,key)

//check if a key exists
	elem, ok := m[key]
	
// Map as a hashset
	attended := map[string]bool{
		"student1": true,
		"student2": true,
	}
	
	if attended[student] {
		fmt.Println(student, "has attended the class.")
	}
	
// Map with empty structs (empty structs occupy zero bytes of memory)
	attended2 := map[string]struct{}{
		"studentA": struct{}{},
		"studentB": struct{}{},
	}

//Nested maps
	map[string]map[string]int
```

- slices, maps and functions cannot be used as keys of a map as they are not comparable.

### Pointers

A pointer is a variable that stores the memory address of another variable.
The zero value of a pointer is nil

```Go

// Declaring a pointer
	var p *int
	
// Generating a pointer using & operand
	myString := "Hello"
	myData := &myString
	
// Getting the value stored at the location in a pointer using * dereferencing operand
	newString := *myData
	
// accessing struct fields of a struct passed by reference

	msg := *myStruct.myField //do not use this
	msg := myStruct.myField //Correct
	msg := (*myStrcut).myField //Equivalent to above
	

```

If a pointer points to nothing, it is called a nil pointer. 
If you try to dereference a nil pointer, the program crashes.
Always check for nil values before dereferencing.

### Packages

Every GO program is made up of packages.
A package named "main" has an entrypoint at main() function and be compiled to an executable.
A package by any other name is a library package.

By convention packages are named after their import paths.
Eg: a package at /myprogram/mypackage will have package mypackage as the package name.

However, a directory of Go code can at most have one package name.
All .go files in a single directory must have the same package name.
If they don't the compile will throw an error.

### Modules
At the top level a GO repository contains one or more modules.
Each module comprises of one or more packages.
Each package comprises of one or more GO source files.

However, it is common to have one module per repository.

### Concurrency

The "go" keyword.

```Go
	go doSomething()
```

Channels are a typed thread safe queue. 
Channels allow communication between different goroutines.

```Go

// Create a channel
	ch := make(chan int)

// sending data through a channnel
	ch <- 29
	
// receiving data from a channel
	myData := <- ch
```

The sending channel blocks the current goroutine until another goroutine is ready to receive the data.
The receiving channel blocks the current goroutines until another there is data to be read.

Both the sending and receiving channels synchronize goroutines.
This can sometimes also lead to deadlocks.

Like maps and slices, channels are too passed by reference.


```Go

// Buffered Channels
	bufferedCh := make(chan int, 200)
```

#### Closing channels

Channels can explicitly closed by a sender.

```Go

// Closing a channel
    ch := make(chan int)

	//send something on the channel
	close(ch)
	
// cheching if a channel is closed.
	val, ok := <- ch
```
Sending on a closed channel will cause a panic. A panic on the main goroutine will crash the program.
While a panic on any other goroutine will crash that goroutine.

Closing is not necessary. Channels will be garbage collected. 
But closing a channel can be used to indicate to a receiver that there is no more data to receive.

#### Range over a channel
Similar to slices and maps, channel can be ranged over.