from sympy import Symbol, lambdify
from functools import reduce
from operator import mul
from numpy import linspace

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def _lagrange_basis(x, xs):
    # xs = [x_0, x_1, ..., x_n] where {x_0, x_n} = {a, b}
    def basis(i):
        li = [(x - xs[j])/(xs[i] - xs[j]) for j in range(xs.size) if i != j]
        return reduce(mul, li)
    return (basis(i) for i in range(xs.size))

def lagrange_basis(n, a=0, b=1, num=100):
    if n > 0:        
        x = Symbol('x')
        xs = linspace(start=a, stop=b, num=n+1)
        basis = _lagrange_basis(x, xs)
        
        x_axis = linspace(a, b, num)
        fig, ax = plt.subplots()
        for i, base in zip(range(xs.size), basis):
            y_axis = lambdify(x, base)(x_axis)
            ax.plot(x_axis, y_axis, label=rf'$\ell_{i}$')
        ax.legend()
        plt.show()
        fig.savefig(f'lagrange-{n}.png')

# plots the lagrange basis of nth order
lagrange_basis(1)
lagrange_basis(2)
lagrange_basis(3)
lagrange_basis(4)
lagrange_basis(5)
