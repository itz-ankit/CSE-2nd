def count(s):
    u= 0
    l= 0
    for char in s:
        if char.isupper():
            u+= 1
        elif char.islower():
            l+= 1
    return u,l

s = input("Enter a string: ")

uppercase, lowercase = count(s)
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")

'''
Enter a string: Archismwan Chatterjee
Uppercase letters: 2
Lowercase letters: 18
'''