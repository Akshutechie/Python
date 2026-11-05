# Operation of sets

set_a = {1,2,3,4}
set_b = {3,4,5,6}

a=set_a|set_b   # Union
b=set_a&set_b   # Intersection
c=set_a-set_b   # Difference between sets
d=set_a^set_b   # Symmmetric difference
e=set_a.issubset(set_b)   # Subset
f=set_a.issuperset(set_b) # Superset

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


set_c={1,2,3,4,5,6}

set_c.add(7)      # Add will add the number to the set
print(set_c)

set_c.remove(1)   # Remove will give error if the number is not present in the set
print(set_c)

set_c.discard(9)  # Discard will not give error if the number is not present in the set
print(set_c)

set_c.pop()
print(set_c)

set_c.update({10,11,12,13})
print(set_c)

empty_set = set()
print(empty_set)

set_c.clear()
print(set_c)

for i in a:
    print(i)

list=set(list[10,10,20,20,30,40,30,40,20,40,50,60,70,70])
print(list)

str="HelloWorld"
print(set(sorted(str)))