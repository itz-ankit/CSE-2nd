a=int(input("Enter lower boundary: "))
b=int(input("Enter upper boundary: "))
sum=0
for i in range(a,b+1,1):
    c=0
    if i==1:
        continue
    for j in range(2,i,1):
        if i%j==0:
            c=1
            break
    if c==0:
        sum=sum+i

print("The sum is: ",sum)

'''
Enter lower boundary: 1
Enter upper boundary: 10
The sum is:  17

'''