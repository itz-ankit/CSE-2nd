a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))

print("The numbers in are \n",a,b,c)


if (a>b and a>c):
    max=a
    if(b>c):
        print("The numbers in sorted order are \n",max,b,c)
    else:
        print("The numbers in sorted order are \n",max,c,b)
elif (b>a and b>c):
    max=b
    if(a>c): 
        print("The numbers in sorted order are \n",max,a,c)
    else:
        print("The numbers in sorted order are \n",max,c,a)
else:
    print ("Maximum is", c )
    if(a>b):
        print("The numbers in sorted order are \n",max,a,b)
    else:
        print("The numbers in sorted order are \n",max,b,a)

'''
Enter 1st number : 12
Enter 2nd number : 34
Enter 3rd number : 2
The numbers in are 
12 34 2
The numbers in sorted order are
34 12 2

'''
