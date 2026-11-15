import numpy as np
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
        if f(x,y)==0 and g(x,y)==0:
            print("Real root found")
            break
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
            print("it is below than eps")
            break
    print(f'Roots x = {x} | y = {y} Answer: f(x,y) = {f(x,y)} | g(x,y) {g(x,y)}')
    print(f'Iterations: {iterations}')
    if iterations>0:
        print(f'Error: {error}')
Solver(-1,0.2,1000,0.0001)