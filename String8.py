# Q. Write a fuction to validate a given password  (1) 8 to 12 digits  (2) Lowercase  (3) Uppercase  (4) Special Characters  (5) Digits

def is_password(n: str):
    if len(n)<8:
        return False

    lower=False
    upper=False
    digit=False
    special=False

    special_chr=set('!@#$%^&*')

    for i in n:
        if i.islower():
            lower=True
        elif i.isupper():
            upper=True
        elif i.isdigit():
            digit=True
        elif i in special_chr:
            special=True

    return lower and upper and digit and special

s=input()
print(is_password(s))