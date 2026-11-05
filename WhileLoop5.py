# Check if a given number is a Armstrong number or not.

n = int(input())
temp = n

print()

# Power

pow = 0

while(n!=0):
    n//= 10
    pow +=1

# Accessing every digit
arm = 0
while(temp!=0):
    ld = n%10
    arm += (ld)**(pow)
    n//= 10

if(arm == check):
    print("Yes")
else 
