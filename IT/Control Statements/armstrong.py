n=int(input("Enter a number"))
sum=0

digit=len(str(n))
t=n

while True:
    p=1
    if t==0:
        break
    d=t%10
    for i in range(1,digit+1,1):
        p*=d
    sum+=p
    t=t//10

if sum==n:
    print('The given number is an Armstrong Number')
else:
    print('Not an armstrong number')
  
'''

Enter a number153
The given number is an Armstrong Number

'''