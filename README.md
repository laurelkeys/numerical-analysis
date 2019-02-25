# numerical-analysis
Scripts developed to implement concepts seen in Unicamp's Numerical Analysis course, MS211.

See below a quick explanation of each:
- [ivp-ode-numerical-methods](#ivp-ode-numerical-methods)
- [lagrange-basis](#lagrange-basis)

## ivp-ode-numerical-methods
Runs a generic method for solving Initial Value Problems (Ordinary Differential Equations) in the form:

$\begin{cases}
    y' = f(x, y)\\
    y(x_0) = y_0
\end{cases}$

[Euler's method](https://en.wikipedia.org/wiki/Euler_method) and Runge-Kutta's fourth order method [RK4](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge%E2%80%93Kutta_method) are implemented.

### Example
To run [Wikipedia's first illustration](https://en.wikipedia.org/wiki/Euler_method#Example) of Euler's method, simply:
```
>>> run_method(4, 1, lambda x, y: y, x0=0, y0=1, method=euler)
y_1: 2
y_2: 4
y_3: 8
y_4: 16
```

## lagrange-basis
Plots the [Lagrange basis polynomials](https://en.wikipedia.org/wiki/Lagrange_polynomial#Definition) of $n^{th}$ order.

### Example
```
>>> lagrange_basis(4)
```
![Output](https://i.imgur.com/g64tFg4.png)

