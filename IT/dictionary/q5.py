
unsorted= {'A': 50, 'B': 30, 'C': 40, 'D': 20}

sorted_dict= dict(sorted(unsorted.items(), key=lambda item: item[1]))

print("Sorted Dictionary in Ascending Order :")
for key, value in sorted_dict.items():
    print(key, value)

'''
Sorted Dictionary in Ascending Order :
D 20
B 30
C 40
A 50
'''