import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 2*x**3-11.7*x**2+17.7*x-5
def df(x):
    return 6*x**2-23.4*x+17.7
def f2(x):
    return -1+5.5*x-4*x**2+0.5*x**3
def df2(x):
    return 1.5*x**2-8*x+5.5-1
def f3(x):
    return x**6-x-1
def Real_Root(coeficients,root,f,index):
    roots=np.roots(coeficients)
    real_roots=np.sort(roots[np.isreal(roots)]).real
    print(f'Real Roots: {real_roots}')
    answer=real_roots[index]
    print(f'Real Root: {answer} Answer: {f(answer)} ',end=' ')
    if root is not None:
        errorS=abs((answer-root)/answer)
        print(f"ErrorS: {errorS}")
def Plotter(root,f,label_f):
    x=np.linspace(-10,10,500)
    y=f(x)
    plt.plot(x,y,color="blue",label=label_f)
    if root is None:
        return
    x_real=root
    y_real=f(x_real)
    plt.scatter(x_real,y_real,color='red',label="Root")
def Bisection_Method(a,b,n,f,eps=0):
    iterations=0
    while iterations<n:
        if f(a)*f(b)>0:
            return None
        mid=(a+b)/2
        if f(mid)==0:
            print("Real root found")
            break
        elif f(a)*f(mid)<0:
            b=mid
        else:
            a=mid
        iterations+=1
        errorA=abs((b-a)/2)
        if errorA<eps:
            print("it is below eps")
            break
    print(f'Root: {mid} Answer: {f(mid)} Iterations: {iterations}')
    if iterations>1:
        print(f"ErrorA: {errorA}")
    return mid
def Newton_Raphson(x0,f,df,n,eps=0):
    iterations=0
    old_x0=None
    
    while iterations<n:
        if df(x0)==0:
            return None
        if f(x0)==0:
            print("Real root found")
            break
        iterations+=1
        old_x0=x0
        x0=old_x0-f(x0)/df(x0)
        errorA=abs((x0-old_x0)/x0)
        if errorA<eps:
            print("It is below eps")
            break
    print(f'Root: {x0} Answer: {f(x0)} ErrorA: {errorA} Iterations: {iterations}')
    if old_x0 is not None and iterations>1:
        print(f'ErrorA: {errorA}')
    return x0
def Secant_Method(x0,x1,f,n,eps=0):
    iterations=0
    
    while iterations<n:
        if f(x1)-f(x0)==0:
            return None
        errorB=abs(x1-x0)
        if errorB<eps:
            print("it below than eps")
            break
        temp=x1
        x1=x0-f(x0)*(x1-x0)/(f(x1)-f(x0))
        iterations+=1
        x0=temp
        if f(x1)==0:
            print("Real root found")
            break
    print(f'Root: {x1} Answer: {f(x1)} Iterations: {iterations}')
    print(f'ErrorB: {errorB}')
    return x1
        
        
root=Secant_Method(1,1.5,f3,100,0.001)
Real_Root([1,0,0,0,0,-1,-1],root,f3,1)
Plotter(root,f3,"-1+5.5*x-4*x**2+0.5*x**3")
plt.axhline(color="black")
plt.axvline(color="black")
plt.grid()
plt.legend()
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show()

        
