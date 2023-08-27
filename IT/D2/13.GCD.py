n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))

while n1 != n2:
    if n1 > n2:
        n1 -= n2
    else:
        n2 -= n1

print(f'GCD is {n1}')
