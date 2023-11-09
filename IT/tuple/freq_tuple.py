t=(1,2,2,4)
c=0
for i in range(4):
    for j in range(4):
        if(t[i]==t[j]):
            c+=1
    print(t[i],c)
    c=0

'''
1 1
2 2
2 2
4 1
'''