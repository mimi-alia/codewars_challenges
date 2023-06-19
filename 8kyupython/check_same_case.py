# Write a function that will check if two given characters are the same case.

#     If either of the characters is not a letter, return -1
#     If both characters are the same case, return 1
#     If both characters are letters, but not the same case, return 0

def same_case(a, b):
    if a.isupper() and b.isupper():
        return 1
    elif a.islower() and b.islower():
        return 1
    elif a.isupper() and b.islower():
        return 0
    elif a.islower() and b.isupper():
        return 0
    else:
        return -1
