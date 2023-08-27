print('Enter the first number')
a = int(input())
print('Enter the second number')
b = int(input())

a = a ^ b
b = a ^ b
a = a ^ b
print(f'a = {a}')
print(f'b = {b}')
