x = 1
for i in range(5):
    for j in range(i+1):
        if i == j:
            print(x, end=' ')
        else:
            print(x, end=',')
        x = x+1
    print()
