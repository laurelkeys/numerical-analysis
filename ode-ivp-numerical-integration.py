import math

def xs(h, x0 = 0):
    x = x0 + h
    while True:
        yield x
        x += h # xi+1 = xi + h

def run_method(func, x0, y0, h, method, iterations):
    print('iteration #1')
    approx = method(x0, y0, h, func)
    print(f'approx: {approx}\n')
    x = xs(h, x0)
    for i in range(2, iterations+1):
        print(f'iteration #{i}')
        approx = method(next(x), approx, h, func)
        print(f'approx: {approx}\n')

def euler(xi, yi, h, f):
    return yi + h*f(xi, yi) # yi+1 = yi + h*f(xi, yi) is an approximation for y(xi)

def rk4(xi, yi, h, f):
    p = f(xi, yi)
    q = f(xi+h/2, yi+p*(h/2))
    r = f(xi+h/2, yi+q*(h/2))
    s = f(xi + h, yi + h*r)
    return yi + (h/6)*(p+2*(q+r)+s)

def exact(xi, yi, h, f):
    return math.e**(-xi+(xi**3)/3)

f = lambda x, y: y*(x**2-1)
it = 4
sol = lambda x: math.e**(-x+(x**3)/3)

print('-> Euler')
run_method(f, 0, 1, 0.25, euler, it)
print('-> RK4')
run_method(f, 0, 1, 0.25, rk4, 4)
print('-> Exact')
x = xs(0.25)
for i in range(1, 4+1):
    print(f'iteration #{i}')
    print(f'solution: {sol(next(x))}\n')
