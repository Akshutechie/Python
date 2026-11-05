# # Recursion is a function calling itself until a condition is satisfied.

# # It's a core mechanism of several algorithm like Back tracking. 

# # Q. Build a recursive function to calculate the factorial of a number

# def fact(n):
#     if n<=0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))


# # Find the sum of numbers from 1 to n using a recursive function
# def sum(n):
#     if n>0:
#      if n==1:
#         return 1
#     return n+sum(n-1)

# print(sum(10))

# Staircase problem : No. of ways of step count 1 + No. of ways by step count 2

# num = int(input())

# def no_ofways(n):
#     if n==1:
#         return 1
#     if n == 2:
#         return 2
#     return no_ofways(n-1)+ no_ofways(n-2)

# print(no_ofways(num))


# Calculate (a)^b using a recursive function and do not use ** or pow() 
#  (i) Repeatative
#  (ii) Base

# a = int(input())
# b = int(input())

# def exp(a,b):
#     if b<=0:
#         return 1
#     return a*exp(a,b-1)

# print(exp(a,b))


# Count the number of digits in a number using recursion.
n=int(input())
def f(n):
    if n<10:
        return 1
    return 1 + f(n//10)

print(f(n))