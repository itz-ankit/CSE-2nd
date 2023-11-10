

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
t1=a
t2=b
while True:
    if a==b:
        break
    else:
        if a>b:
            a-=b
        else:
            b-=a

lcm=t1*t2
print ("LCM of", t1, "and" ,t2,"is:", lcm)

'''

Enter 1st number: 2
Enter 2nd number: 3
LCM of 2 and 3 is: 6

'''