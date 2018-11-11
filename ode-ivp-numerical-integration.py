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

f = lambda x, y: y*(x**2-1)
run_method(f, 0, 1, 0.25, euler, 4)
