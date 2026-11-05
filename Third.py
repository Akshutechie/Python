# Print all the numbers which are divisible bt 3 and 5 from 1 to 100

n = int(input("Enter a value :"))
count = 0
for i in range(1,n+1):
    if(i%3 == 0 and i%5 == 0):
        print(i)
        count +=1
