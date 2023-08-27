print("Enter the principal amount")
p = float(input())

if p < 200000:
    print(0.1*p)
elif p < 1000000:
    print(0.12*p)
else:
    print(0.15*p)
