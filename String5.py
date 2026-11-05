con="Python   is   high  level Programming  "
x=con.strip()
y=x.split(" ")
temp=""
for i in y:
    temp+=i
print(" ".join(temp))
