stars = 9
space = 0

while stars > 0:
    for i in range(space):
        print(' ', end='')
    for i in range(stars):
        print('*', end='')
    stars = stars-2
    space = space+1
    print()
