Data structures:
Data structures are organizational tools that allow for more advanced alogrithms.

Algorithms:
Algorithm is a set of instructions that can be carried out to solve a problem.
Also a finite, sequence of well-defind computer implementable instructions.
Also
1. Defined: there is a sequnce of steps that perform a task
2. unambiguous: there is a "correct" and "incorrect" interpretation of the steps
3, Implementable: it can be executed using software and hardware

## Math:

### Mean and Median
Mean : The average of the numbers in a list of numbers.
Median: The middle number after the list is ordered. or the average of the middle two numbers if the list even no.of items.

  Eg: For a list of [1,3,2,25]
    Mean = 7.75
    Median = [ 1,2,3,25] > mean of 2 and 3 = 2.5

### Geometric progression:
In a sequence of numbers where the first number is 'a' and multiplying factor between any two conesecutive numbers is 'r',
then the 'n'th number in the sequence is => a * r ^ (n-1)

eg: 3 * 12 * 48 * 192
  here a = 3
       r = 4
       then 5th number will be = 3 * (4 ^ (5-1)) = 768
      
**Exponent**: Indicates how many times a number is multiplied by itself.
  Eg: 5^3 = 5 * 5 * 5 = 125

    5^3 is read as "5 to the power of 3"
    5 is the "base"
    3 is the "exponent"
       
### Non linear growth:
If the number of operations grow quickly as the amount of input data increases, the algorithm will become slower and slower.

- The doubling formula, 2*x, results in linear or straight growth. O(2x) - linear growth
- The quadratic formula, x^2, keeps growing faster and faster. O(x^2) - quadratic growth/polynomial growth. (BAD)

### Logarithmic:
A logarithm is an inverse of an exponent.

    2^4 = 16
    log base2 (16) = 4

  Table illustrating the no.of operations based on the type of algorithm per input size
  
  |Input Size   |	Linear (n*2) 	|Quadratic (n^2)        |	Log (log2(n)) | 
  |-------------|---------------|-----------------------|---------------|
  |10 	        |20 ms 	        |100 ms 	              |3 ms           |
  |100 	        |200 ms 	      |10,000 ms 	            |7 ms           |
  |1,000 	      |2,000 ms 	    |1,000,000 ms 	        |10 ms          |
  |10,000 	    |20,000 ms 	    |100,000,000 ms 	      |14 ms          |
  |100,000 	    |200,000 ms 	  |10,000,000,000 ms      |17 ms           |
  |1,000,000 	  |2,000,000 ms 	|1,000,000,000,000 ms   |20             |

### Factorial:
    
    
    0! = 1
    1! = 1
    2! = 2 * 1
    3! = 3 * 2 * 1
    4! = 4 * 3 * 2 * 1
    5! = 5 * 4 * 3 * 2 * 1
    
    5! = 5 * 4! = 5 * (5-1)!
    Hence n! = n*(n-1)!


## Big O notation:
    
    Big O is the characterization of algorithms according to their worst-case growth rates.

  O(n) notation  (Fastest to slowest)

    Excellent                           Fair              Bad
    O(1)      > O(log2(n))  > O(n)    > O(n log2(n))    > O(n^2) | O(n^3) | O(n^4)  > O(2^n)      > O(n!)
    constant  > log         > linear  > super - linear  > quadratic(polynomial)     > exponential > factorial
    
    There is also O(nm). which is slower than O(n) b faster than O(n^2)
    
  Big O vs Algorithms:

  | No.   |Big O       | Algorithms                        |
  |-------|------------|-----------------------------------|
  |1.     |O(1)        |                                   | 
  |2.     |O(logn)     | binary search tree                |
  |3.     |O(n)        |min, max                           |        
  |4.     |O(nlogn)    |Merge sort, Quick sort,                          |
  |5.     |O(n^2)      |nested loop, Bubble sort, Insertion sort           |
  |6.     |O(2^n)      |                                   |
  |7.     |O(n!)       |                                   |

    - Merge sort: Takes Divide and conquer approach. Makes copies . Uses recursion. Affects memory due to copies of split arrays.
    - Insertion sort: Fast for small inputs
    - Quick sort: Suited for larger inputs, Recursive and Divide & conquer algorithm. Doesn't make copies, sorts the elements in place.
                Bad if the list is pre-sorted and can fall to O(n^2). Can be minimized by randomizing the pivot point.
                Use the median of three approach to ensure O(mlogn). Pick the first, last and a middle index to find the median.
