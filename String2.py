# Check whether a given string is Palindrome or not.

s = "ma'am"  
i, j = 0, len(s) - 1  
is_palindrome = True  

while i < j:
    if s[i] != s[j]:  
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("Yes") 
else:
    print("No")

# Remove the spaces from the given string

s2 = "not a palindrome"

for i in s2: 
    if (i!= ' '):
        print(i, end = "")