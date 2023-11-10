a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(f"GCD of {a} and {b} is {gcd(a,b)}")
print(f"LCM of {a} and {b} is {lcm(a,b)}")

'''
Enter the first number: 2
Enter the second number: 6
GCD of 2 and 6 is 2
LCM of 2 and 6 is 6
'''