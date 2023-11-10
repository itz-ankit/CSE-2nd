principal=float(input("Enter the amount "))
time=float(input("Enter the time duration "))

if(principal<200000):
    rate=10.0
    interest=(principal*rate*time)/100
elif(principal>=200000 and principal < 1000000):
    rate=12.0
    interest=(principal*rate*time)/100
else:
    rate=15.0
    interest=(principal*rate*time)/100

print("The interest is Rs. ", interest)


'''
Enter the amount 200000
Enter the time duration 1
The interest is Rs.  24000.0
'''


