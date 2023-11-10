l=[1,2,3,4,5,6,7,8,2,2]
even=lambda x:x%2==0
print("The even numbers are: ")
final=filter(even,l)
for i in final:
    print(i)
'''
The even numbers are: 
2
4
6
8
2
2
'''
