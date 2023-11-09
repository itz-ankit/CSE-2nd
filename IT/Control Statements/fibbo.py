a=int(input("Enter lower boundary: "))
b=int(input("Enter upper boundary: "))
sum=0
for i in range(a,b+1,1):
    f=0
    for j in range(2,(int)((i/2)+1)):
        if (i%j==0):
            f=1
            break
    if f==0:
        sum+=i

print(sum)            

'''
Enter lower boundary: 1
Enter upper boundary: 10
18

'''