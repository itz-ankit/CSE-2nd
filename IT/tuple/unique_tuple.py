list1=[1,2,4,5,6,2,5]
t=sorted(list1)
print(t)
u=0
s=0
for i in range(len(list1)-1):
    if(t[i]==t[i+1]):
        s+=1
    else:
        u+=1
print(s,u)
'''
[1, 2, 2, 4, 5, 5, 6]
2 4
'''