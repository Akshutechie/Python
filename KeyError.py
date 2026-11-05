# Q. Asking a dictionary for a key that does not

l1 = [10,20,30,40,50]

def list_ele_print(l1,index):
    try:
        print(l1[index])
    except IndexError:
        print(f"Given Range of Index : {index} is out of Range")

list_ele_print(l1,8)