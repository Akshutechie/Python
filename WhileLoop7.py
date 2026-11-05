# Find the largest digit from the given number (if the given number is always positive)

n = int(input())

largest = -1

while(n!=0):
    ld =n%10
    if(largest < ld):
         largest = ld
    n //=10

print(sum)

# Find the smallest digit from the given number (if the given number is always positive)

n = int(input())

smallest = 9

while(n!=0):
    ld =n%10
    if(smallest > ld):
         smallest = ld
    n //=10

print(sum)

