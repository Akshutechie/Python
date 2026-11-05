n=int(input("Enter a integer number: "))
print(f"Prime number between 1 and {n} is: ")

for num in range(2,n+1):
    factor_count=0
    for i in range(1,num+1):
        if(num%i==0):
            factor_count+=1
    if factor_count==2:
        print(num,end=" ")


