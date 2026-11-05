# Q. Write a function to swap the first and last element  of given tuple

def swap(t):
    if len(t)==1:
        return t
    result=((t[-1],)+(t[1:-1])+(t[0],))
    return result

t=(10, 20, 30, 40, 50)

swap(t)

# Write a function to reverse a given tuple

t1=(10,)
def rev(t):
    result=t[::-1]
    return result

print(rev(t1))

# Write a function to rotate the given tuple by K positions
def rot(t, k):
    k=k%len(t)
    r=((t[-k:])+t[:-k])
    return r

print(rot(t, 2))