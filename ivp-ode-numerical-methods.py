import math

###### methods execution

# subdivides the analysed interval [a, b] into n parts (uniform mesh)
step = lambda n, a, b: (b-a)/n

def xs(h, x0 = 0):
    x = x0 + h
    while True:
        yield x
        x += h # x_i+1 = x_i + h

def run_method(n, h, func, x0, y0, method):
    # IVP ODE:
    #  | y' = func(x, y)
    #  | y(x_0) = y_0
    approx = method(x0, y0, h, func)
    print(f'y_1: {approx}')
    x = xs(h, x0)
    for i in range(2, n+1):
        approx = method(next(x), approx, h, func)
        print(f'y_{i}: {approx}')

###### methods

def euler(xi, yi, h, f):
    # y_i+1 = y_i + h*f(x_i, y_i) where y_i is an approximation for y(x_i)
    return yi + h*f(xi, yi)

def rk4(xi, yi, h, f):
    p = f(xi, yi)
    q = f(xi+h/2, yi+p*(h/2))
    r = f(xi+h/2, yi+q*(h/2))
    s = f(xi + h, yi + h*r)
    return yi + (h/6)*(p+2*(q+r)+s)

###### methods usage

f = lambda x, y: y*(x**2-1)
iv = (0, 1) # initial values (x_0, y_0)
sol = lambda x: math.e**(-x+(x**3)/3) # exact solution of the ODE y'=f

n = 4
h = 0.25

print('-> Given')
print(f'[a, b] = [x_0, x_n] = [{iv[0]}, {iv[0]+n*h}]') # x_n = x_0 + n*h
print(f'y_0 = y(x_0) = {iv[1]}')
print(f'x_0 = {iv[0]}')
x = xs(h, iv[0])
for i in range(1, n+1):
    print(f'x_{i} = {next(x)}')

print('\n-> Exact')
x = xs(h, iv[0])
for i in range(1, n+1):
    print(f'y(x_{i}): {sol(next(x))}')

print('\n-> Euler')
run_method(n, h, f, x0=iv[0], y0=iv[1], method=euler)

print('\n-> RK4')
run_method(n, h, f, x0=iv[0], y0=iv[1], method=rk4)

# note:
#   if we want a fixed interval [a, b] with n subdivisions then h is calculated as
#   h = (b-a)/n = step(a, b, n)
#   => n is the number of subintervals: [a, b]=[x_0, x_n] with subintervals [x_i, x_i+1]
#   however, if we want the first n values starting on a=x_0 with x_i+1 = x_i + h
#   then we also provide the value of h
#   => n is the number of desired values: y_0, y_1, ..., y_n
