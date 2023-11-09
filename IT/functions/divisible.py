a=int(input("Enter lower range: "))
b=int(input("Enter upper range: "))
c=lambda x: x % 5 == 0 and x % 7 == 0

print([num for num in range(a,b + 1,1) if c(num)])

'''
Enter lower range: 10
Enter upper range: 100
[35, 70]
'''