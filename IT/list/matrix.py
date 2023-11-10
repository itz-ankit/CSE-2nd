X=[[1,0,0],[0,1,0],[0,0,1]]
Y=[[1,0,0],[0,1,0],[0,0,1]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range (len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]
print(result)

'''
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
'''