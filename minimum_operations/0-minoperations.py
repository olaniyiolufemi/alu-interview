#!/usr/bin/python3

def minOperation(n):
    if n <= 1:
        return 0
    
    num_of_operations = 0  # Initialize num_of_operations to 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n // divisor  # Use integer division (//) instead of float division (/)
            num_of_operations += 1  # Increment num_of_operations by 1, not divisor
        else:
            divisor += 1

    return num_of_operations

n = 12
print(minOperation(n))