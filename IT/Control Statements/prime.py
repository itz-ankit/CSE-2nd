n=int(input("Enter a number : "))
c=0
for i in range(2,n,1):
    if n%i==0:
        c=1
        print("The number is not prime: ",n)
        break
if c==0:
    print("The number is prime: ",n)

'''
1) Enter a number : 45
   The number is not prime:  45

2) Enter a number : 11
   The number is prime:  11
'''