p=0
co=0
while True:
    c=0
    num=int(input("Enter number"))
    if num==-1:
        print("Found")
        break
    if num==1:
        continue
    if num<0:
        num*=-1
    for i in range(2,num,1):
        if num%i==0:
            c=1
            break
    if c==0:
        p+=1
    else:
        co+=1

print("Prime:",p,"Composite:",co)

'''
Enter number2
Enter number4
Enter number1
Enter number5
Enter number8
Enter number-1
Found
Prime: 2 Composite: 2

'''
    