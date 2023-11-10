s = input("Enter a string: ")

print("The substrings are \n")
for i in range(len(s)+1):
    print(s[:i],"\t")
for i in range(len(s)+1):
    print(s[i:],"\t")

'''
A 
Ar 
Arc 
Arch
Archi
Archis
Archism
Archismw
Archismwa
Archismwan
Archismwan
rchismwan
chismwan
hismwan
ismwan
smwan
mwan
wan
an
n

'''