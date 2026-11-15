def Maximum(scalar,matrix):
    for i in range(len(matrix)):
        scalar[i]=max(abs(matrix[i][k]) for k in range(len(matrix)))
def Forward(matrix,vector):
    scalar=[0]*len(matrix)
    Maximum(scalar,matrix)  
    for k in range(len(matrix)-1):
        max_raw=None
        max_element=-1
        for m in range(k,len(matrix)):
            if abs(matrix[m][k]/scalar[m])>max_element:
                max_element=abs(matrix[m][k]/scalar[m])
                max_raw=m
        matrix[k],matrix[max_raw]=matrix[max_raw],matrix[k]
        vector[k],vector[max_raw]=vector[max_raw],vector[k]
        scalar[k],scalar[max_raw]=scalar[max_raw],scalar[k]
        for i in range(k+1,len(matrix)):
            
            
            factor=matrix[i][k]/matrix[k][k]
            
            for j in range(len(matrix[i])):
                matrix[i][j]=matrix[i][j]-factor*matrix[k][j]
            vector[k]=vector[k]-vector[k]*factor
def Backward(matrix,vector):
    x=[0]*len(matrix)
    for k in range(len(matrix)-1,-1,-1):
        sum=vector[k]
        for j in range(k,len(matrix)):
            sum-=matrix[k][j]*x[j]
        x[k]=sum/matrix[k][k]
    return x
matrix=[
    [1,1,-1],
    [6,2,2],
    [-3,4,1]
]
vector=[-3,2,1]
Forward(matrix,vector)
x=Backward(matrix,vector)
print(matrix)
print(vector)
print(x)