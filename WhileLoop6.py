#Calculate the sum of all the digits of a given number

n = int(input())

sum = 0

while(n!=0):
    ld =n%10
    sum += ld
    n //=10

print(sum)

