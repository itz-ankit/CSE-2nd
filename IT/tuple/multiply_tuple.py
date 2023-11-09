l=(1,2,3,3,5)
c=0
for i in range(0,len(l)-1):
    p=l[i]*l[i+1]
    if p%2==0:
        print("Answer is ",p)
        c+=1
if c==0:
    print("No such pair found")

print(c,"pairs found")
'''
Answer is  2
Answer is  6
2 pairs found

'''