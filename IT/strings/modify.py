s=input("Enter a word: ")

ch = s[-1]
s = s[:-1].replace(ch, '*')+ch

print(s)

'''
Enter a word: Mess
Me*s

'''