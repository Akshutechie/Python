# Q. Write a function to remove duplicates from a given string

def remove_duplicates(s):
    s.strip()
    temp=""
    for i in s:
        if i not in temp:
            temp+=i
    return temp

du=remove_duplicates("RamaRamaRama")
print(du)

# Q. Write a function to count and print the longest word in the given string

def count_and_print_longest_word(text):
    
    words = text.strip().split()
    
    if not words:
        print("No words found.")
        return
  
    longest_word = max(words, key=len)
      
    print(f"The longest word is: '{longest_word}' with a length of {len(longest_word)}.")


sentence = "   First Programme Language   "
count_and_print_longest_word(sentence)   