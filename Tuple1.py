# Q. Write a function to print all the elements of the given beside it's index:  Sample Output : 0 : 10
#                                                                                                1 : 20
#                                                                                                2 : 30
# Print the maximum, minimum and avearge of given tuple

t=(10,20,30,40)
def tup(t):
    for i in range(len(t)):
        print(f"{i} : {t[i]}")

    sum_tup=sum(t)
    print(min(t))
    print(max(t))
    print(sum_tup/len(t))

tup(t)

# Q. Write a function to remove an element from a tuple without converting it to a list 

