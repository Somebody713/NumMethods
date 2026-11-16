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

# def f1(x,y,z):
#     return x+y-z-3
# def f2(x,y,z):
#     return x**2+y**2+z**2-5
# def f3(x,y,z):
#     return np.exp(x)+x*y-x*z-1
# def Jacobian(x,y,z):
#     return np.array([
#         [1,1,-1],
#         [2*x,2*y,2*z],
#         [np.exp(x)+y-z,x,-x]
#     ])
# def Solver(x,y,z,n,eps):
#     iterations=0
    
#     while iterations<n:
#         F=np.array([f1(x,y,z),f2(x,y,z),f3(x,y,z)])
#         J=Jacobian(x,y,z)
#         delta=np.linalg.solve(J,-F)
#         x=x+delta[0]
#         y=y+delta[1]
#         z=z+delta[2]
#         iterations+=1
#         error=np.linalg.norm(delta)
#         if error<eps:
#             print("It below than eps")
#             break
#     print(f'Roots x = {x} | y = {y} | z = {z}')
#     print(f'Answers: f1 = {f1(x,y,z)} | f2 = {f2(x,y,z)} | f3 = {f3(x,y,z)}')
#     print(f'Iterations: {iterations}')
#     if iterations>0:
#         print(f'Error: {error}')
# Solver(2,2,2,50,10**-4)

# def f(x):
#     return -0.6*x**2+2.4*x+5.5
# def f2(x):
#     return x**2*abs(np.cos(np.sqrt(x)))-5
# def f3(x):
#     return x**4-8*x**3-35*x**2+450*x-1001
# def Real_Root(root,coeficients):
#     roots=np.roots(coeficients)
#     real_roots=np.sort(roots[np.isreal(roots)].real)
#     answer=real_roots[1]
#     if root is None:
#         return
#     errorS=abs((answer-root)/answer)
#     print(f'ErrorS: {errorS}')
# def NonLinear_Real_Root(root,f):
#     answer=sci.fsolve(f,root)[0]
#     if  root is None:
#         return
#     errorS=abs((answer-root)/answer)
#     print(f'ErrorS: {errorS}')
# def Bisection_Method(a,b,f,n,coeficients,eps=0):
#     iterations=0
#     old_c=None
#     if f(a)==0:
#         c=a
#     elif f(b)==0:
#         c=b
#     while iterations<n:
#         if f(a)*f(b)>0:
#             return None
#         c=(a+b)/2
#         if f(a)*f(c)<0:
#             b=c
#         elif f(c)*f(b)<0:
#             a=c
#         else:
#             print("Real root found")
#             break
#         if old_c is not None:
#             errorA=abs((c-old_c)/c)
#             print(f'ErrorA: {errorA}')
#             Real_Root(c,coeficients)
#         old_c=c
#         iterations+=1
#         error=abs(b-a)/2
#         if error<eps:
#             print("it belows eps")
#             break
#     print(f'Root: {c} Answer: {f(c)} Iterations: {iterations}')
#     if iterations>0:
#         print(f'Error: {error}')
#     return c
# root=Bisection_Method(4.5,6,f3,5,[1,-8,-35,450,-1001],0.01) 
# x=np.linspace(-10,10,500)
# y=f3(x)
# plt.plot(x,y,color="green",label="Function")
# plt.scatter(root,f3(root),color="red",label="Root")
# plt.axhline(color="black")
# plt.axvline(color="black")
# plt.ylabel("f(x)")
# plt.xlabel("x")
# plt.grid(True)
# plt.legend()
# plt.show()
       

# def Taylor_PI(n,eps=0):
#     result=0
#     term=None
#     iterations=0
#     while iterations <n:
#         if term is not None:
#             if abs(term)<eps:
#                 print("It belows eps")
#                 break
#         term=((-1)**iterations*4)/math.factorial(2*iterations+1)
#         iterations+=1
#         result+=term
#     print(f"Result : {result} Iterations: {iterations}")
# Taylor_PI(1000,0.001)

# def Maclaurian_Series(a,b,eps=0.01):
#     iterations=0
#     result=0
#     for i in range(-1,2):
#         term=(-1)**i/(2**i)
#         iterations+=1
#         result+=term
#         if abs(term)<eps:
#             print("It belows eps")
#             break
#     print(f'Result: {result} Iterations: {iterations}')
# Maclaurian_Series(-1,1)      

# def f(x,a,b):
#     return a*x+b
# def f2(x,a,b,c):
#     return a+b*x+c*x**2
# def f3(x,a,b,c,d):
#     return a*x**3+b*x**2+c*x+d
# def Curve_Fit(x,y):
#     A=np.array([
#         [np.sum(x**6),np.sum(x**5),np.sum(x**4),np.sum(x**3)],
#         [np.sum(x**5),np.sum(x**4),np.sum(x**3),np.sum(x**2)],
#         [np.sum(x**4),np.sum(x**3),np.sum(x**2),np.sum(x)],
#         [np.sum(x**3),np.sum(x**2),np.sum(x),len(x)]
#     ])
#     B=np.array([np.sum(x**3*y),np.sum(x**2*y),np.sum(x*y),np.sum(y)])
    
#     params=np.linalg.solve(A,B)
#     return params
# def Error(x,y,f,params):
#     residuals=[0]*len(x)
#     error=0
#     for i in range(len(x)):
#         residuals[i]=(f(x[i],*params)-y[i])**2
#         error+=residuals[i]
#     print(f'Error: {error}')
#     return residuals
# x=np.array([1,2,3,4,5,6,7,8,9])
# y=np.array([2,-4,8,1,9,4,5,2,0])
# x_plot=np.linspace(np.min(x),np.max(x),500)
# real_params=sci.curve_fit(f3,x,y)[0]
# params=Curve_Fit(x,y)
# residuals=Error(x,y,f3,params)
# y_plot=f3(x_plot,*real_params)
# plt.plot(x_plot,y_plot,color="blue",label="Real Curve")
# plt.plot(x_plot,f3(x_plot,*params),color="green",label="My Curve")
# plt.scatter(x,y,color="red")
# plt.axvline(color="black")
# plt.axhline(color="black")
# plt.grid(True)
# plt.legend()
# plt.show()

# def MaxInRow(matrix):
#     scalar=[0]*len(matrix)
#     for i in range(len(matrix)):
#         scalar[i]=np.max([abs(matrix[i][k]) for k in range(len(matrix))])
#     return scalar
# def Forward(matrix,vector):
#     scalar=MaxInRow(matrix)
#     for k in range(len(matrix)-1):
#         max_element=0
#         max_row=0
#         for m in range(len(matrix)):
#             if abs(matrix[m][k]/scalar[m])>max_element:
#                 max_element=matrix[m][k]/scalar[m]
#                 max_row=m
#         matrix[k],matrix[max_row]=matrix[max_row],matrix[k]
#         vector[k],vector[max_row]=vector[max_row],vector[k]
#         scalar[k],scalar[max_row]=scalar[max_row],scalar[k]
#         for i in range(k+1,len(matrix)):
            
#             factor=matrix[i][k]/matrix[k][k]
            
#             for j in range(k,len(matrix)):
#                 matrix[i][j]=matrix[i][j]-factor*matrix[k][j]
#             vector[i]=vector[i]-vector[k]*factor
# def Backward(matrix,vector):
#     x=[0]*len(matrix)
#     for i in range(len(matrix)-1,-1,-1):
#         sum=vector[i]
#         for j in range(i,len(matrix)):
#             sum-=matrix[i][j]*x[j]
#         x[i]=sum/matrix[i][i]
#     return x
# matrix=[
#     [1,1,-1],
#     [6,2,2],
#     [-3,4,1]
# ]
# vector=[-3,2,1]
# Forward(matrix,vector)
# answers=Backward(matrix,vector)
# print(matrix)
# print(vector)
# print(answers)


def f(x,y):
    return np.sin(x+1)-y-1.2
def g(x,y):
    return 2*x+np.cos(y)-2
def Jacobian(x,y):
    return np.array([
        [np.cos(x+1),-1],
        [2,-np.sin(y)]
    ])
def Solver(x,y,n,eps=0):
    
    iterations=0
    while iterations<n:
        F=np.array([
            f(x,y),
            g(x,y)
        ])
        J=Jacobian(x,y)
        delta=np.linalg.solve(J,-F)
        x=x+delta[0]
        y=y+delta[1]
        iterations+=1
        error=np.sqrt(delta[0]**2+delta[1]**2)
        if error<eps:
            print("It belows eps")
            break
    print(f'Roots : x = {x} y = {y} Answers: f(x,y) = {f(x,y)} g(x,y) = {g(x,y)}')
    print(f'Error: {error}')
Solver(1,2,100,0.0001)
        