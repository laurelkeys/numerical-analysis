
# numerical-analysis
Scripts developed to implement concepts seen in Unicamp's Numerical Analysis course, MS211.

See below a quick explanation of each:
- [ivp-ode-numerical-methods](#ivp-ode-numerical-methods)
- [lagrange-basis](#lagrange-basis)
- [lotka-volterra](#lotka-volterra)
- [lu-decomposition-with-pivoting](#lu-decomposition-with-pivoting)
- [lu-decomposition](#lu-decomposition)
- [tridiagonal-lu-decompostion](#tridiagonal-lu-decompostion)

## ivp-ode-numerical-methods
Runs a generic method for solving Initial Value Problems (Ordinary Differential Equations) in the form:

![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20y%27%20%3D%20f%28x%2C%20y%29%5C%5C%20y%28x_0%29%20%3D%20y_0%20%5Cend%7Bcases%7D)

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

## lagrange_basis
Plots the [Lagrange basis polynomials](https://en.wikipedia.org/wiki/Lagrange_polynomial#Definition) of $n^{th}$ order.

### Example
```
>>> lagrange_basis(4)
```
![Output](https://i.imgur.com/g64tFg4.png)

## lotka-volterra

## lu-decomposition-with-pivoting
Solves a linear equation in the form ![](https://latex.codecogs.com/gif.latex?A%20x%20%3D%20b) by performing the LU (lower–upper) decomposition of a matrix with [partial pivoting](https://en.wikipedia.org/wiki/LU_decomposition#LU_factorization_with_partial_pivoting).

### Example
Running `decompose_and_solve(A, b)` returns `(P, L, U, y, x)` such that:
![](https://latex.codecogs.com/gif.latex?PA%20=%20LU)
where
![](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bcases%7D%20Ly%20%3D%20Pb%20%5C%5C%20Ux%20%3D%20y%20%5Cend%7Bcases%7D)


```
>>> decompose_and_solve([[4,3],[6,3]], [4,6])
(
 [[0.0, 1.0], 
  [1.0, 0.0]], 
 [[1.0, 0.0], 
  [0.6666666666666666, 1.0]], 
 [[6.0, 3.0], 
  [0.0, 1.0]], 
 [6.0, 0.0], 
 [1.0, 0.0]
)
```

## lu-decomposition
## tridiagonal-lu-decompostion
