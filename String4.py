# Q. Check if the given string is a palindrome or not.

# str=input()
# rev=str[::-1]
# if str==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Q. Write a program that extracts the domain name from the given string. 

# b = input()
# for i in b.split("@"):
#     if i=="rungta.org":
#         print(i) 

# s="keshav.kumar@rungta.org"
# s1 = s.split("@")[1]
# print(s1)

# Q. Write a program to split the string at first 2 colons only
# "name:age:city:country"
# ss="aaa:20:bhootiya:bhoot"
# print(ss.split(":",2))


# Q. Noramlize the given string :

con="Python   is   high  level Programming  "
word=con.split()
normalize=" ".join(word)
print(normalize)
