a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
print("The numbers before swapping are",a,b)
a=a^b
b=a^b
a=a^b 
print("The numbers after swapping are",a,b)

'''
Enter 1st number 10
Enter 2nd number 20
The numbers before swapping are 10 20
The numbers after swapping are 20 10

'''