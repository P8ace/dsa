# Go Programming Language

[GO by example](https://gobyexample.com/)

Go is a statically typed, compiled, memory safe and garbage collected programming language.  
Go has high speed compilation and excellent tooling support.

## Comments

```Go
// Single line comments

/* 
Multi
Line 
Comments
*/
```

* * *

## Constants

Go supports constants of character, string, boolean and numeric values.

```go
package main

// keyword const declares a constant value
const value string = "Hello there!"

func main() {
    // const can also be used inside a function
    const myConst string = "Another Constant"

    // const expression
    const d = 3e20/5000
}

```

* * *

## Variables

```go
package main

func main() {
    // type inference
    var a = "initial"

    // declaring multiple variables at once
    var b,c = 2, 3

    // variables declared without initialized will be initialzed to their zero values. 
    // For ints its 0, for strings "", for booleans false
    var d int

    // short hand syntax for declaration and initialization.
    // short hand syntax is only valid within a function.
    e := "five"
}
```

Rules for Naming Variables

1.  Variable names must start with a letter or underscore (\_).
2.  Names can contain letters (a-z, A-Z), digits (0-9), and underscores \_.
3.  Variable names cannot start with a digit.
4.  Variable names are case-sensitive: geeks and Geeks are different.
5.  Keywords cannot be used as variable names.
6.  No strict limit on length, but 4–15 characters is recommended.

### Zero values for variables.

1.  0 for numeric types
2.  false for boolean
3.  "" for strings
4.  nil for reference and interface types  
    reference based data types:
    1.  slices
    2.  maps
    3.  channels

* * *

## Data types

### Basic datatypes in Go.

- Numeric:
    - uint, uint8, uint16, uint32, uint64
        
    - uintptr (width undefined, can hold all bits of a pointer value)
        
    - int, int8, int16, int32, int64
        
        ```
          byte is an alias for int8 type
          rune is an alias for int32 type
        ```
        
    - float32, float64
        
    - complex64, complex128
        
- string
- bool

```go
    max(a,b)
    min(a,b)
    
    // built-in functions to work with complex numbers
    var a complex64 = complex(6,9)
    data = real(a)
 	imaginary = imag(a)
```

* * *

### Operators

```go
//Arithmetic Operators
+, _, *, /, %

a + b
a - b
a / b
a * b
a % b
 
//Relational Operators
==, !=, >, <, >=, <=

//Logical Operators
&&, ||, !

// Assignment Operators
// =, +=, -=, *=, /=, %=, 

// Bitwise Operators
// & bitwise and
// | bitwise or
// ^ bitwise xor
// << left shift
// >> right shift
// &^ bit clear operator


```

### Value based Composite data types

Arrays and structs combine other data types.

#### Arrays:

An array is a fixed length sequence of homogenous elements in memory. Elements in an array can be accessed using their index position. Arrays in Go are 0-based.

```Go
    // declaring an array of integers of length 10.
    // by default all elements will be initialized to their zero val.
    var a [10]int

    // declaring and initializing an array of 5 integers
    b := [5]int{1,2,3,4,5}

    // inferring the length of the integer array.
    c := [...]int{6,7,8,9,0}

    // accessing an element in an array at index 1
    elem := c[1]

    // modifying or setting an element in array
    c[3] = 11

    // declaing an array with elements leaving some of them
    testarr := [...]int{1,2, 4:100, 500}
    // will be printed as [1,2,0,0,100,500]

    // multi dimensional array
    arr := [3][3]int{{1,2,3}, {4,5,6}, {7,8,9}}
    arr2 := [2][3]int{{1,2,3}, {4,5,6}}

    // finding the length of an array
    length := len(c)
```

#### Structs

Structs are defined after functions section.

* * *

### Pointers

A pointer is a variable that stores the memory address of another variable.  
The zero value of a pointer is nil

```Go
    // Declaring a pointer
    var p *int

    // Referencing
    // Generating a pointer using the derefencing(&) operator.
    var myString stirng = "Hello"
    var myData *string = &myString

    // Dereferencing
    // Getting the value stored at the location in a pointer using dereferencing(*) operator
    newString := *myData

    // Modifying a pointer will update the value at original location
    a := "mydata"
    b := &a
    *b = "newdata"
    fmt.Println(a)	// will print "newdata"

    // the built-in "new" function returns a pointer to a type
    ab := new(int)
    // is equivalent to
    var ab *int = new(int)
    fmt.Println(*ab) // will print 0
    
// accessing fields of a struct passed by reference
    msg := *myStruct.myField //do not use this
    msg := myStruct.myField //Correct way to use
    msg := (*myStruct).myField //Equivalent to above
    
```

If a pointer points to nothing, it is called a nil pointer.  
If you try to dereference a nil pointer, the program crashes.  
Always check for nil values before dereferencing.

* * *

### Reference data types.

Reference based composite data types.  
Zero values of a reference based data type is nil.

- Slices
- Maps
- Channel  
    All of the above are also composite data types as they are composed of other basic data types.  
    All of the above can be created with the built-in make function.

#### Slices

Zero value of a slice is nil.

```Go
    // declaring a slice of ints
    var a []int

    // creating a slice with built-in make function.
    s := make([]string,len:3,cap:10)
    t := make([]int, 4)
    // 4 is used as both length and capacity

    // declare and intialize a slice (slice literal syntax)
    b := []int{1,2,3,4,5}

    // accessing an element from a slice
    data := b[2]

    // setting/modifying an element in a slice
    b[3] = 100
    func myfunc(){
        printNumbers(b...)
    }

    // length and capacity of a slice using built-in function
    length := len(b)
    capacity := cap(b)

    // setting all elements to zero-values
    clear(b)

    // copying the underlying data from one slice to another
    copyb := make([]int, len(b))
    n := copy(copyb, b)

    // subslices using slice operator
    s := []int{4,5,6,7,8}
    a := s[4:]
    
    // string to a slice
    data := []rune(word) //word is a string, being converted to a slice of runes(int32)

    // built-in append function appends elements to the end of slice
    s = append(s, 9)
    fmt.Println(s) //will print [4,5,6,7,8,9]
    t := []int{10,11,12}
    s = append(s, t...)
    fmt.Println(s) //will print [4,5,6,7,8,9,10,11,12]
```

#### Maps

Zero value of a map is nil.  
Maps are associative data types, that associate keys with values.

```go
// Creating a amp
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
    
// Get an element, also returns a boolean. false if not found.
    elem:= m[key]

//check if a key exists
    elem, ok := m[key]
// if key doesnt exist, ok will be false and a zero-value is returned
    
// Delete an element
    delete(m,key)

// delete all keys and values for an empty map
    clear(m)

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
- Maps are not thread safe. Use mutexes

* * *

### Loops

```Go
    // for INITAL; CONDITION; AFTER {}
    for i:= 0; i <10; i++{
        fmt.Println(i)
    }

    // for CONDITION {}
    data = 10
    for data > 5 {
        //do something
        data--
    }

    //or simply a forever loop 
    for {
        //do something
        continue // go to next iteration
        //do semething
        break // stop the current iteration and exit the loop
    }

    #### Range function
    for n := range 6{
        fmt.Print(n) // will print 0,1,2,3,4,5
    }

    // traversing a slice/array
     for INDEX, ELEMENT := range SLICE/array {}
     // ignoring the index value
     for _, element := range slice/array {}

     // traversing a map
     for key, value := range mymap {}
     // iterating over just keys
     for key := range mymap{}
     // ignoring keys 
     for _, val := range mymap{}

     // iterating over strings
     for _, rune := range mystring {}
```

## Functions

```Go
    //declaring a function
    func plus(a int, b int) int{
        return a + b
    }

    // consecutive parameters of same type can ignore type name
    func plus(a, b int) int{
        return a + b
    }

    // returning multiple values
    func vals() (int, int){
        return 4,5
    }
    
    //variadic functions accept any number of arguments
    func print(str ...int) {
        for s := str{
            fmt.Println(s)
        }
    }

    // passing a slice to a variadic function
    nums := []int{1,2,3,4}
    print(nums...)
```

## Structs

A struct is a user defined type that allows to group/combine elements of different types into a single datatype.

```go
// defining a struct
type Address struct {
    name string
    street string
    city string
    state string
    pincode int32
}

// declaring and initializing a struct variable
address1 := Address{
    name : "Akshay",
    street : "Prem Nagar",
    city : "Gurugram",
    state : "Haryana",
    pincode : 1244356
}

// accessing a field of a struct using the dot(.) operator
fmt.Println(address1.name)
fmt.Println(address1.city)

// modifying or setting a field of a struct
address1.state = "Punjab"

//Nested structs
type Author struct{
    name string
    branch string
    year 	int16
}

type HR struct {}
    details Author 
}

ourHr = HR{
    details : Author {
        name : "SOSO",
        branch : "Their branch",
        year	: "9999"
    }
}

// or
detailedAuthor := Author {
        name : "SOSO",
        branch : "Their branch",
        year	: "9999"
}
ourHR = HR {
    details : detailedAuthor
}

//accessing fields of a nested structure
result := hr.details.name

//anonymous structs
var test_case := struct{
    input int,
    expected int
} {
    input : 20,
    expected : 400
}

// struct embedding
type Student struct {
    name string
    class string
}

type College struct{
    name string
    city string
    Student
}
```

## Error Interface:

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

## Concurrency

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
The receiving channel blocks the current goroutines until there is data to be read.

Both the sending and receiving channels synchronize goroutines.
This can sometimes also lead to deadlocks.

Like maps and slices, channels are too passed by reference.


```Go

// Buffered Channels
	bufferedCh := make(chan int, 200)
```

#### Closing channels

Channels can be explicitly closed by a sender.

```Go

// Closing a channel
    ch := make(chan int)

	//send something on the channel
	close(ch)
	
// checking if a channel is closed.
	val, ok := <- ch
```
Sending on a closed channel will cause a panic. A panic on the main goroutine will crash the program.
While a panic on any other goroutine will crash that goroutine.

Closing is not necessary. Channels will be garbage collected. 
But closing a channel can be used to indicate to a receiver that there is no more data to receive.

#### Range over a channel
Similar to slices and maps, channel can be ranged over.

```Go
	for data := range ch{
		//do something
	}
```
This will block at each iteration and will only break the loop once the channel is closed.

#### Select

```Go

	select {
	case i, ok := <-chInts:
			if ok {
				fmt.Println(i)
			}
	case s, ok := <-chStrings:
			if ok {
				fmt.Println(s)
			}
	}
	
// A default case in a select statement will execute if no channels have data to recieve
// It stops the select statement from blocking

	select {
		case v := <- ch : 
			// do something with v
		default:
			// do something else
			
	}
````

### Mutex
Short for Mutual exclusion. Excludes from different thread/goroutines from accessing the same data at the same time.

```Go
	func protected() {
		mu.Lock()
		defer mu.Unlock()
		//the rest of the function
	}
````

RW Mutex

    Read and Write Lock. It also has Lock and Unlock methods. In addition, it also has RLock and RUnlock. RLock and RUnlock methods allow for 
    multiple readers to read the data at the same time, but any writers will have to wait for the lock to be unlocked.

```Go
	func protected() {
		rw.RLock()
		defer rw.RUnlock()
	}
```


## Panic and Recover

When a function calls panic, the program crashes and prints the stack trace.  
The panic function removes the control out of the current function and up the stack trace until it reaches a  
defered recover() function. If there is no recover function in the stack, the program crashes.

* * *

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

### Generics

```Go
    func splitslice[T any](s []T)([]T, []T){
        mid = len(s)/2
        return s[:mid], s[mid:]
    }
// any in the signature is a constraint. 

// Using type lists/sets as constraints

type Ordered interface{
    ~int8 | ~int16 | ~int32 | ~int64 
}	

func Min[T Ordered](a, b T)(T){
    if a < b {
        return a
    }
    return b
}

    
```

### Go Proverbs

```
Don't communicate by sharing memory, share memory by communicating.

Concurrency is not parallelism.

Channels orchestrate; mutexes serialize.

The bigger the interface, the weaker the abstraction.

Make the zero value useful.

interface{} says nothing.

Gofmt's style is no one's favorite, yet gofmt is everyone's favorite.

A little copying is better than a little dependency.

Syscall must always be guarded with build tags.

Cgo must always be guarded with build tags.

Cgo is not Go.

With the unsafe package there are no guarantees.

Clear is better than clever.

Reflection is never clear.

Errors are values.

Don't just check errors, handle them gracefully.

Design the architecture, name the components, document the details.

Documentation is for users.

Don't panic.
```
