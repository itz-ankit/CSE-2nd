s=input("Enter a sentence: ")
w=input("Enter the word: ")
s = s.split(" ")
c=0
for i in range(0, len(s)):         
        
        if (w == s[i]):
           c+=1

print("The occurence of ",w,"in ",s," is :",c)

'''
Enter a sentence: Hi I am Archismwan Chatterjee 
Enter the word: Chatterjee
The occurence of  Chatterjee in  ['Hi', 'I', 'am', 'Archismwan', 'Chatterjee', '']  is : 1

'''