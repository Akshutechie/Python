s= lambda x,y : x+y         # Sum
print(s(4,9))

s = lambda x : x**2         # Square
print(s(4))

# Factorial of a number

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    print(fact)

factorial(5)