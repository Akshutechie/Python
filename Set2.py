# Q. Write a funtion to print the no. of distinct words in a given sentence. 

s="The cat and the hat"
def distinct_words(s):
    conv_s=s.lower().split()
    result=len(set(conv_s))
    return result

print(distinct_words(s))
