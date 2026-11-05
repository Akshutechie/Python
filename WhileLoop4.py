# Print all the digits of a given number
# Count the number of digits for a given number


n = int(input())

print()
count = 0

while (n!=0):
    ld = n %10
    print(ld)
    n //= 10
    count += 1

print(count)


