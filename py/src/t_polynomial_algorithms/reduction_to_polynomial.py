"""
Broadly speaking, algorithms can be classified into two categories:

    "Polynomial time"
    "Exponential time"
An algorithm runs in "Polynomial time" if its runtime does not grow faster than n^k, where k is any constant (e.g. n^2, n^3, etc)
and n is the size of the input. Polynomial-time algorithms can be useful if they're not too slow.

In comparison, exponential-time algorithms are almost always too slow to be practical.
(However, sometimes you're trying to force someone to be slow, like in the case of cryptography and security).
Even when n is as low as 20, 2^n is already over a million!

Let's take an exponential time algorithm and fix it up so it can run in polynomial time!

Lets sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

Modify the fib function which is exponential to a polynomial time.

    The input n represents the index of the desired Fibonacci number.
    If n is less than or equal to 1, then return n.
    Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
    Write a loop that iterates n - 1 times. (For example, if n = 2, one iteration occurs.)
    Inside the loop:
        Set current = parent + grandparent
        Adjust the ancestor values (parent and grandparent) to maintain the sequence.
    Once the loop completes, return current.


"""
# 0, 1, 2, 3, 4, 5, 6, 7,  8,   9
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = 0 
    for i in range(n-1): #2 0,1
        current = parent + grandparent # at i=0 current 1   | at i=1 current=2  | at i =2 current=3 | at i=3 current=5
        grandparent = parent           # at i=0 gp 1        | at i=1 gp 1       | at i=3 gp 2
        parent = current               # at i=0 p 1         | at i=1 p  2        | at i=3  p 3
    return current