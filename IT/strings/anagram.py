a=input("Enter the first string: ")
b=input("Enter the second string: ")

if sorted(a) == sorted(b):
    print("The given words are Anagram")
    
else:
    print("The given words are not Anagram")

'''
Enter the first string: gram
Enter the second string: amrg
The given words are Anagram
'''