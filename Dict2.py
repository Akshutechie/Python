# Write a function to print the key which holds the maximum value

# d1={'x':-1, 'y':-10, 'z':-7}
# def max_value(dic):
#    lar=-1*2**32
#    for key, value in dic.items():
#     if value>lar:
#         lar=value
#     return key

# print(max_value(d1))


# Write a function to merge_add(d1,d2) two dictionaries and check if the given key is same and there values (i) Default - Same Length

d1={'a':1,'b':10}
d2={'b':2,'c':4}
def merge_add(d1,d2):
   for key, value in d1.items():
    if key in d2:
        d2[key]=d2[key]+value
    else:
        d2[key]=value
    
    return d2

print(merge_add(d1,d2))