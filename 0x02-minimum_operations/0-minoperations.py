#!/usr/bin/python3

"""
    minOperationd file for less road 
"""

def minOperations(n):

    # If n is 1 or less, no operations are needed or possible
    if n <= 1:
        return 0

    operations = 0  # This will store the total number of operations needed
    divisor = 2     # Start with the smallest possible divisor (2)
    
    # Keep dividing n by the current divisor as long as it's divisible
    while n > 1:
        while n % divisor == 0:   # While n is divisible by 'divisor'
            operations += divisor  # Add the divisor to the count of operations
            n //= divisor          # Reduce n by dividing it by the divisor
        divisor += 1               # Move to the next divisor
    
    return operations
