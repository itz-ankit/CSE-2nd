
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))

if x > y:
    small = y
else:    
    small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

print ("G.C.D of", x,"and", y ,"is:", gcd)

'''
Enter 1st number: 2
Enter 2nd number: 6
G.C.D of 2 and 6 is: 2

'''