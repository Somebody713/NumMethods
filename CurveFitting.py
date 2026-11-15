import numpy as np
import scipy.optimize as sci
import matplotlib.pyplot as plt

def f1(x,a,b,c):
    return a*np.cos(x)+b*np.exp(x)+c
def f2(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d
def f3(x,a,b,c):
    return a+b*np.sin(x)+c*x**3
def Plotter(x,f,params,color_f,label_f):
    x_plot=np.linspace(np.min(x),np.max(x),500)
    y_plot=f(x_plot,*params)
    plt.plot(x_plot,y_plot,color=color_f,label=label_f)
    
def Find_Parametrs1(x,y):
    A=[
        [np.sum(np.cos(x)),np.sum(np.exp(x)),len(x)],
        [np.sum(np.exp(x)*np.cos(x)),np.sum(np.exp(2*x)),np.sum(np.exp(x))],
        [np.sum(np.cos(x)**2),np.sum(np.exp(x)*np.cos(x)),np.sum(np.cos(x))]
    ]
    B=[np.sum(y),np.sum(y*np.exp(x)),np.sum(y*np.cos(x))]
    
    params=np.linalg.solve(A,B)
    return params
def Find_Parametrs2(x,y):
    A=[
        [np.sum(x**6),np.sum(x**5),np.sum(x**4),np.sum(x**3)],
        [np.sum(x**5),np.sum(x**4),np.sum(x**3),np.sum(x**2)],
        [np.sum(x**4),np.sum(x**3),np.sum(x**2),np.sum(x)],
        [np.sum(x**3),np.sum(x**2),np.sum(x),len(x)]
    ]
    B=[np.sum(y*x**3),np.sum(y*x**2),np.sum(y*x),np.sum(y)]
    params=np.linalg.solve(A,B)
    return params
def Find_Parametrs3(x,y):
    A=[
        [len(x),np.sum(np.sin(x)),np.sum(x**3)],
        [np.sum(np.sin(x)),np.sum(np.sin(x)**2),np.sum(np.sin(x)*x**3)],
        [np.sum(x**3),np.sum(np.sin(x)*x**3),np.sum(x**6)]
    ]
    B=[np.sum(y),np.sum(y*np.sin(x)),np.sum(y*x**3)]
    params=np.linalg.solve(A,B)
    return params
def Error(x,y_real,f,params):
    y=f(x,*params)
    return np.sum((y_real-y)**2)
x=np.array([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5])
y=np.array([-1,-0.7,0.2,1.5,2.1,3.2,3.5,3.6,3.3,3.6,4.2,5.7])
params1=Find_Parametrs1(x,y)
params2=Find_Parametrs2(x,y)
params3=Find_Parametrs3(x,y)
error1=Error(x,y,f1,params1)
error2=Error(x,y,f2,params2)
error3=Error(x,y,f3,params3)
print(f'Parametrs1: a = {params1[0]} | b = {params1[1]} | c = {params1[2]}')
print(f'Error1: {error1}')
Plotter(x,f1,params1,"green","a*np.cos(x)+b*np.exp(x)+c")
print(f'Parametrs2: a = {params2[0]} | b = {params2[1]} | c = {params2[2]} | d = {params2[3]}')
print(f'Error2: {error2}')
Plotter(x,f2,params2,"grey","a*x**3+b*x**2+c*x+d")
print(f'Parametrs3: a = {params3[0]} | b = {params3[1]} | c = {params3[2]}')
print(f'Error3: {error3}')
Plotter(x,f3,params3,"blue","a+b*np.sin(x)+c*x**3")
real_params1=sci.curve_fit(f1,x,y)[0]
real_params2=sci.curve_fit(f2,x,y)[0]
real_params3=sci.curve_fit(f3,x,y)[0]
a_real,b_real,c_real=real_params1
print(f'Real Parametrs1: a = {a_real} | b = {b_real} | c = {c_real}')
a_real,b_real,c_real,d_real=real_params2
print(f'Real Parametrs2: a = {a_real} | b = {b_real} | c = {c_real} | d = {d_real}')
a_real,b_real,c_real=real_params3
print(f'Real Parametrs3: a = {a_real} | b = {b_real} | c = {c_real}')
plt.scatter(x,y,color="red")
plt.axvline(color="black")
plt.axhline(color="black")
plt.grid(True)
plt.legend()
plt.show()

