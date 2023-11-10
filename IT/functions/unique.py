def unique(l):
    u= []
    
    for i in l:
        if i not in u:
            u.append(i)
    
    return u

# Input a list from the user (comma-separated values)
l= input("Enter a list of elements separated by commas: ").split(',')

# Call the function to find unique elements
unique= unique(l)

# Display the unique elements
print("Unique elements in the list:", unique)

'''
Enter a list of elements separated by commas: 1,2,3,5,6,2
Unique elements in the list: ['1', '2', '3', '5', '6']
'''