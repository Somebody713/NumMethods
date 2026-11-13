import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return -0.6*x**2+2.4*x+5.5
def df(x):
    return -1.2*x+2.4
def f2(x):
    return 4*x**3-6*x**2+7*x-2.3
def f3(x):
    return x**2-3
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
    old_mid=None
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
        if old_mid is not None:
            errorA=abs((mid-old_mid)/mid)
            if errorA<eps:
                print("it is below eps")
                break
        old_mid=mid
    print(f'Root: {mid} Answer: {f(mid)} Iterations: {iterations}')
    if old_mid is not None and iterations>1:
        print(f"ErrorA: {errorA}")
    return mid
    
root=Bisection_Method(-3,1,100,f3,0.0001)
Real_Root([1,0,-3],root,f3,1)
Plotter(root,f3,"x**2-3")
plt.axhline(color="black")
plt.axvline(color="black")
plt.grid()
plt.legend()
plt.ylabel("f(x)")
plt.xlabel("x")
plt.show()

        
