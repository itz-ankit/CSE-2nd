s=input("Enter a sentence: ")

a,e,i,o,u=0,0,0,0,0
for x in s.lower():
    if x == 'a':
        a+=1
    if x == 'e':
        e+=1
    if x == 'i':
        i+=1
    if x == 'o':
        o+=1
    if x == 'u':
        u+=1                

print("The Number of \n","a=",a,"e=",e,"i=",i,"o=",o,"u=",u)

'''
Enter a sentence: Hi I am Archismwan Chatterjee
The Number of 
a= 4 e= 3 i= 3 o= 0 u= 0
'''
