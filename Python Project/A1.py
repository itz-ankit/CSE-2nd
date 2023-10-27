n = int(input())
if n % 2 == 0:
    index = n // 2
    result = 2 ** index
else:
    index = n // 2
    result = 3 ** index

print(result)
