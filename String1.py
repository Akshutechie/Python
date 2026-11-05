st12 = "Hello World"

for i in st12:
    print(i)

for j in range(len(st12)):
    print(st12[j])

print(st12[0:11])
print(st12[0:5])
print(st12[::-1])

# Reverse a string using loops

s = "Hello"
for i in range(len(s)-1,-1,-1):
    print(s[i],end = " ")

# Convert uppercase to lower case letters and lower case to upper case for a given string

s1 ="This is topics of string"

for i in s1:
    if(i.isupper() == True):
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")

