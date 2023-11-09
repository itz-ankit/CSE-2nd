n = int(input("Enter the number of players: "))

cricket = {}

for i in range(n):
    name = input("Enter player's name: ")
    runs = int(input("Enter runs scored: "))
    cricket[name] = runs

print(cricket)

name = input("Enter player's name to get runs scored: ")

runs = cricket.get(name, -1)

if runs == -1:
    print("-1")
else:
    print(f"{name} has scored {runs} runs.")

'''
Enter the number of players: 3
Enter player's name: Virat
Enter runs scored: 100
Enter player's name: Gill
Enter runs scored: 100
Enter player's name: A
Enter runs scored: 20
{'Virat': 100, 'Gill': 100, 'A': 20}
Enter player's name to get runs scored: Virat
Virat has scored 100 runs.
'''
