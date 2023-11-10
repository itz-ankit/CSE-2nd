name=["A","B","C","D"]
sal=["1000","2000","3000","4000"]
d={}
for i in range(len(name)):
    d[name[i]] = sal[i]

#d=dict(zip(name, sal))

print(d)
'''
{'A': '1000', 'B': '2000', 'C': '3000', 'D': '4000'}
'''