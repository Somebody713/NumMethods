import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.optimize as sci

# def f(x):
#     return x**2*np.sin(-2*x)
# def Taylor_Series(x,n):
#     result=0
    
#     for i in range(n):
#         result+=(-1)**i*(-2)**(2*i+1)*x**(2*i+3)/(math.factorial(2*i+1))
#         print(f'Iteration: {i+1} = {np.max(result)} | Real Answer: {np.max(f(x))}')
#         print(f'Error: {np.max(abs(f(x)-result))}')
#     return result
# x=np.linspace(-1,1,500)
# y_real=f(x)
# y_Taylor=Taylor_Series(x,5)
# plt.plot(x,y_real,color="green",label="Real")
# plt.plot(x,y_Taylor,color="grey",label="Taylor")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.axvline(color="black")
# plt.axhline(color="black")
# plt.grid(True)
# plt.legend()
# plt.show()


# def f(x):
#     return np.exp(-x)*(x**2+5*x+2)+1
# def df(x):
#     return -np.exp(-x)*(x**2+5*x+2)+np.exp(-x)*(2*x+5)
# def Newton_Raphson(x,n,f,df,eps=0):
#     iterations=0
    
#     while iterations<n:
#         if(df(x)==0):
#             return None
#         if(f(x)==0):
#             print("Real root found")
#             break
#         x_old=x
#         x=x_old-f(x_old)/df(x_old)
#         iterations+=1
#         error=abs(x-x_old)
#         if abs(f(x))<eps:
#             print("It belows eps")
#             break
#     print(f"Root: {x} | Answer: {f(x)} Iterations: {iterations}")
#     if iterations>0:
#         print(f'Error: {error}')
#     return x
# def Secant_Method(x0,x1,n,f,eps):
#     iterations=0
    
#     while iterations<n:
#         if f(x1)-f(x0)==0:
#             return None
#         if f(x1)==0:
#             print("Real root found")
#             break
#         x2=x0-f(x0)*(x1-x0)/(f(x1)-f(x0))
#         x0=x1
#         x1=x2
#         iterations+=1
#         error=abs(x1-x0)
#         if error<eps:
#             print("It belows eps")
#             break
#     print(f"Root Secant: {x1} | Answer Secant: {f(x1)} Iterations: {iterations}")
#     if iterations>0:
#         print(f'Error Secant: {error}')
#     return x1
# x=np.linspace(-1,1,500)
# y=f(x)
# root_Newton=Newton_Raphson(0,1000,f,df,0.0001)
# root_Secant=Secant_Method(-1,0,1000,f,0.0001)
# real_root=sci.fsolve(f,0)[0]
# print(f'Real Root: {real_root} Answer: {f(real_root)}')
# plt.scatter(root_Newton,f(root_Newton),color="red",label="Newton Root")
# plt.scatter(root_Secant,f(root_Secant),color="grey",label="Secant Root")
# plt.plot(x,y,color="green",label="func")
# plt.axhline(color="black")
# plt.axvline(color="black")
# plt.grid(True)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.title("Newton and Secant")
# plt.show()

def f1(x,y,z):
    return x+y-z-3
def f2(x,y,z):
    return x**2+y**2+z**2-5
def f3(x,y,z):
    return np.exp(x)+x*y-x*z-1
def Jacobian(x,y,z):
    return np.array([
        [1,1,-1],
        [2*x,2*y,2*z],
        [np.exp(x)+y-z,x,-x]
    ])
def Solver(x,y,z,n,eps):
    iterations=0
    
    while iterations<n:
        F=np.array([f1(x,y,z),f2(x,y,z),f3(x,y,z)])
        J=Jacobian(x,y,z)
        delta=np.linalg.solve(J,-F)
        x=x+delta[0]
        y=y+delta[1]
        z=z+delta[2]
        iterations+=1
        error=np.linalg.norm(delta)
        if error<eps:
            print("It below than eps")
            break
    print(f'Roots x = {x} | y = {y} | z = {z}')
    print(f'Answers: f1 = {f1(x,y,z)} | f2 = {f2(x,y,z)} | f3 = {f3(x,y,z)}')
    print(f'Iterations: {iterations}')
    if iterations>0:
        print(f'Error: {error}')
Solver(2,2,2,50,10**-4)
        
        
    