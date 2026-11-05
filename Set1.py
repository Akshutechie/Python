a=[1,2,3]
b=[2,3,4,5]
def unique(a,b):
    x=set(a)
    y=set(b)
    return list((x|y) - (x&y))

print(unique(a,b))
    
    
