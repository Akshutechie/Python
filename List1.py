l1 = [10,20,30,40,50,60,70,80,90,100]
t1 = (10,20,30,40,50,60,70,80,90,100)

print(l1[5:])
print(t1[5:])
print(l1[-4])
print(t1[-4])

# Comprehension method of declaring a list

# x = [Expression loop-statement condition]
        # 3           1               2
 
l2=[i for i in range(1,1001)]
print(l2) 

# Create a list in which we have to print all even numbers from 1 to 50

l3=[i for i in range(1,51) if i%2==0] 
print(l3)


# Create a list that contains only the cubes of odd numbers from list [101 to 130]

l4=[i**3 for i in range(101,131) if i%2!=0]
print(l4)

#Create a list that contains only the cubes of odd numbers from given list l5
l5=[55,67,98,200,101]
print([i**3 for i in l5 if i%2!=0])

# Create a list and append
l6=[10,20,30,40,50]
l6.append(33)
print(l6)
l6.remove(10)
print(l6)
print(len(l6))
print(min(l6))
print(max(l6))
print(sum(l6))
