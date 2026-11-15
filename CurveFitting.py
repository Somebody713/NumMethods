import numpy as np
import scipy.optimize as sci

def f1(x,a,b,c):
    return a*np.cos(x)+b*np.exp(x)+c
def Find_Parametrs1(x,y):
    A=[
        [np.sum(np.cos(x)),np.sum(np.exp(x)),len(x)],
        [np.sum(np.exp(x)*np.cos(x)),np.sum(np.exp(2*x)),np.sum(np.exp(x))],
        [np.sum(np.cos(x)**2),np.sum(np.exp(x)*np.cos(x)),np.sum(np.cos(x))]
    ]
    B=[np.sum(y),np.sum(y*np.exp(x)),np.sum(y*np.cos(x))]
    
    params=np.linalg.solve(A,B)
    return params
def Error(x,y_real,f,params):
    y=f(x,params[0],params[1],params[2])
    return np.sum((y_real-y)**2)
x=np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
y=np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7])
params=Find_Parametrs1(x,y)
error=Error(x,y,f1,params)
print(f'Parametrs: a = {params[0]} | b = {params[1]} | c = {params[2]}')
print(f'Error: {error}')
real_params=sci.curve_fit(f1,x,y)[0]
a_real,b_real,c_real=real_params
print(f'Real Parametrs: a = {a_real} | b = {b_real} | c = {c_real}')
