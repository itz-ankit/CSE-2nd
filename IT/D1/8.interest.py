p = float(input("Enter the principal amount\n"))
r = float(input("Enter the interest rate\n"))
t = int(input("Enter the duration\n"))

a = p*(1+r*t/100.0)

print(f'Interest Amount : {a-p}')
print(f'Total Amount : {a}')
