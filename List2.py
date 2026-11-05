# Q1. Write a function to check what elements gives the target sum in the given list :  {1st question of leet code; DSA}
# Sample test case

target = 9
L = [1,2,3,4,5,8]
seen=set()
def target_sum(target):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]+L[j]==target:
                print(L[i],L[j])


target_sum(target)


# Write a function to move all the zeroes present in the given list while keeping the same order L = [0,1,0,3,12]
# Output will be : [1,3,12,0,0]

l1=[0,1,0,3,12]
def list_sorting(li):
   non_zeroes= [x for x in li if x!=0]
   zeroes=[0]*li.count(0)
   return non_zeroes+zeroes

print(list_sorting(l1))