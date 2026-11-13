def Forward(matrix,vector):
    for k in range(len(matrix)-1):
        for i in range(k+1,len(matrix)):
            
            factor=matrix[i][k]/matrix[k][k]
            
            for j in range(len(matrix[i])):
                matrix[i][j]=matrix[i][j]-factor*matrix[i-1][j]
            vector[i]=vector[i]-vector[i-1]*factor
    
matrix=[
    [2,-1,0,0],
    [-1,2,-1,0],
    [0,-1,2,-1],
    [0,0,-1,1]
]
vector=[1,0.5,1,2]
Forward(matrix,vector)
print(matrix)
print(vector)