# Check that the given number is perfect number

import math

def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 is always a proper divisor
    # Iterate from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            # Add the corresponding divisor if it's different
            if i != n // i:
                divisor_sum += n // i
                
    return divisor_sum == n

# Example usage
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is NOT a Perfect Number")   