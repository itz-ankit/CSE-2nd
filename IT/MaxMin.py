l=input("Enter the elements of the list followed by spaces: ").split()
max=int(l[0])
min=int(l[0])
for i in l:
    current=int(i)
    if(current>max):
        max=current
       
    if(current<min):
        min=current
        
print("\nMaximum element is:",max)        
print("Min element is:",min)
