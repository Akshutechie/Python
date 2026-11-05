# Write a function to count each characters and print it in a dictionary 

word = "banana"

def count_freq(word):
    empty_dict = {}

    for i in word:
        if i in empty_dict:
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1
    return empty_dict

print(count_freq(word))
