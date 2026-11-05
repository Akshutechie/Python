# Check whether a number is prime or not using while loop

n = int(input("Enter a num : "))

i = 1
count = 0
while(i<=n):
    if(n%i == 0):
        count +=1
    i+=1

if(count == 2):
    print(f"Given number {n} is prime number")
else:
    print(f"Given number {n} is Not prime number")