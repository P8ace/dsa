'''
Given a large number return a list of all the prime factors.
'''
import math

def prime_factors(n):
    result = []
    
    while n%2==0:
        n = n/2
        result.append(2)
    
    limit = math.sqrt(n)
    for i in range(3, int(limit) + 1, 2):
        if n%i==0:
            n = n/i
            result.append(i)
    
    if n > 2:
        result.append(n)
        
    return sorted(result)
        