import numpy as np
def Find_Parametrs(x,y):
    A=[
        [np.sum(np.cos(x)),np.sum(np.exp(x)),len(x)],
        [np.sum(np.exp(x)*np.cos(x)),np.sum(np.exp(2*x)),np.sum(np.exp(x))],
        [np.sum(np.cos(x)**2),np.sum(np.exp(x)*np.cos(x)),np.sum(np.cos(x))]
    ]
    B=[np.sum(y),np.sum(y*np.exp(x)),np.sum(y*np.cos(x))]
    
    params=np.linalg.solve(A,B)
    return params
x=np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
y=np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7])
params=Find_Parametrs(x,y)
print(params)