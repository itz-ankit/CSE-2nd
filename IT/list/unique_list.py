list1=input().split()
list2=input().split()

list=[x for x in list2 if x not in list1]

print(list)

'''
1 2 3 4 5 
6 7 4 1 
['6', '7']

'''