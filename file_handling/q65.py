
# File line order reverse:

with open('file2.txt','r') as f:
    l=f.readlines()
    with open('file3.txt','w') as file:
        l.reverse()
        file.writelines(l)

# File content reverse:

with open('file2.txt','r') as f:
    l=f.read()
    l=l[::-1]
    print(l)
    with open('file4.txt','w') as file:
        file.write(l)


