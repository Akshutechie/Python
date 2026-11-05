# Find the sum of factors of a number

n = int(input())

for i in range(1,n+1):
    if(n%i == 0):
        total = total + i  #total += i (both are same)
        print(total)
        

