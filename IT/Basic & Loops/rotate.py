x=float(input("Enter the 1st number "))
y=float(input("Enter the 2nd number "))
z=float(input("Enter the 3rd number "))

print ("The numbers before rotating are ", x, y , z)

temp=z
z=y
y=x
x=temp

print ("The numbers after rotating are ", x, y , z)

'''
Enter the 1st number 10
Enter the 2nd number 20
Enter the 3rd number 30
The numbers before rotating are  10.0 20.0 30.0
The numbers after rotating are  30.0 10.0 20.0
'''