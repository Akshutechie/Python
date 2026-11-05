# User defined function
# Steps

# (i) def func_name ():
# (ii) Function Call
# (iii) Execute

def hello():                
    print("hello world")    
hello()

# Define a function to print the name of a Student

def name():
    print("Akshu")
name() 

def multiply(a,b):
    print(a*b)

def m2(a,b):
    return a*b

multiply(12,2)

x = m2(12,2)
print("MSD", x)

# Write a function to print a list

l = [10,20,30,40,50]       # Global Scope

def pl(E):
    for i in E:            # Indentation Scope
        print(i)           # Local Scope
pl(l)


x = 10

def pr():
    global x
    x = 9
    print(x)

print(x)

pr()

print("new line")

pr()


