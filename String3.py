s1 = "  Recursion is very useful  "       # Strip removes extra spaces 
s2 = s1.strip()
print(s2)

s3 = s1.lstrip()                          # Remove extra spaces from left hand side
print(f"lstrip : {s3}")

s4 = s1.rstrip()                          # Remove extra spaces from right hand side
print(f"rstrip : {s4}")

s5 = s1.split()
print(s5)

s6 = "Apple,Mango,Banana"
s7 = s6.split(",",1)
s8 = s6.split(",",2)
print(s7)
print(s8)
