
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

## lagrange-basis
Plots the [Lagrange basis polynomials](https://en.wikipedia.org/wiki/Lagrange_polynomial#Definition) of n<sup>th</sup> order.
### Example
```
>>> lagrange_basis(4)
```
![Output](https://i.imgur.com/g64tFg4.png)

## lotka-volterra
Solves [Lotka–Volterra](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)'s predator–prey nonlinear differential equations numerically.

This was developed as a course project and it's report can be [read here](https://github.com/laurelkeys/numerical-analysis/blob/master/ms211-projeto-2.pdf) (in portuguese).

## lu-decomposition-with-pivoting
Solves a linear equation in the form ![](https://latex.codecogs.com/gif.latex?A%20x%20%3D%20b) by performing the LU (lower–upper) decomposition of a matrix with [partial pivoting](https://en.wikipedia.org/wiki/LU_decomposition#LU_factorization_with_partial_pivoting).
### Example
Running `decompose_and_solve(A, b)` returns `(P, L, U, y, x)` such that ![](https://latex.codecogs.com/gif.latex?PA%20=%20LU), where:

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
Solves a linear equation in the form ![](https://latex.codecogs.com/gif.latex?A%20x%20%3D%20b) by performing the [LU (lower–upper) decomposition](https://en.wikipedia.org/wiki/LU_decomposition) of a matrix without pivoting.
### Example
Running `decompose_and_solve(A, b)` returns `(L, U, y, x)`, such that ![](https://latex.codecogs.com/gif.latex?A%20=%20LU), after printing L, U and their dot product.
```
>>> decompose_and_solve([[4,3],[6,3]], [4,6])
[[1.0, 0.0], 
 [1.5, 1.0]]
[[4, 3], 
 [0.0, -1.5]]
array([[4., 3.],
       [6., 3.]])
(
 [[1.0, 0.0], 
  [1.5, 1.0]], 
 [[4, 3], 
  [0.0, -1.5]], 
 [4.0, 0.0], 
 [1.0, -0.0]
)
```


## tridiagonal-lu-decompostion
Performs the LU decomposition of a [tridiagonal matrix](https://en.wikipedia.org/wiki/Tridiagonal_matrix) to solve a linear equation in the form ![](https://latex.codecogs.com/gif.latex?A%20x%20%3D%20b) (thus it is optimized and faster than using **lu-decomposition**).
### Example
Running `tridiagonal_decompose_and_solve(A, b)` returns `(L, U, y, x)`, such that ![](https://latex.codecogs.com/gif.latex?A%20=%20LU), after printing L, U and their dot product.
```
>>> tridiagonal_decompose_and_solve([[4,3],[6,3]], [4,6])
[[1.0, 0.0], 
 [1.5, 1.0]]
[[4, 3], 
 [0.0, -1.5]]
array([[4., 3.],
       [6., 3.]])
(
 [[1.0, 0.0], 
  [1.5, 1.0]], 
 [[4, 3], 
  [0.0, -1.5]], 
 [4.0, 0.0], 
 [1.0, -0.0]
)
```
