n=10
for i in range(1,n+1):
    if i==4:
        break
    print(i)

print( )

n=10
for i in range(1,n+1):
    if (i%2==0):
        continue    # Skip
    print(i)

print( )

n=6
for i in range(1,n+1):
    if i==4:
        pass
    print(i)