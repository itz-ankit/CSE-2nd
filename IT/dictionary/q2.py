word=input("Enter a word: ")
d={}
c=0 #counter
for i in range(len(word)):
    for j in range(len(word)-1):
        if(word[i]==word[j]):
            c+=1
        d[word[i]]=c
        c=0
print(d)
'''
Enter a word: archismwan
{'a': 1, 'r': 0, 'c': 0, 'h': 0, 'i': 0, 's': 0, 'm': 0, 'w': 0, 'n': 0}
'''
