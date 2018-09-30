from pprint import pprint
from numpy import dot

def diagonals(A):
  n = len(A)
  a = [0.0 for i in range(n-1)] # lower diagonal (i-j==1)
  b = [0.0 for i in range(n)] # main diagonal (i==j)
  c = [0.0 for i in range(n-1)] # upper diagonal (j-i==1)
  for i in range(n):
    for j in range(n):
      if i-j == 1.0:
        a[i-1] = A[i][j] # a starts with a_2, not a_1
      elif i == j:
        b[i] = A[i][j]
      elif j - i == 1.0:
        c[i] = A[i][j]
  return (a, b, c)

def tridiagonal_lu(A):
    a, b, c = diagonals(A)
    n = len(b) # main diagonal
    L = [[(1.0 if i == j else 0.0) for i in range(n)] for j in range(n)]
    U = [[(1.0 if i == j else 0.0) for i in range(n)] for j in range(n)]
    for i in range(n-1):
      for j in range(n):
        if j - i == 1.0:
          U[i][j] = c[i]
    
    U[1][1] = b[1]
    for k in range(1, n):
      L[k][k-1] = a[k-1]/U[k-1][k-1] # we use a[k-1] instead of a[k] since a starts at a_2, not a_1
      U[k][k] = b[k] - L[k][k-1]*c[k-1]
    
    return (L, U)

def forward_substitute(L, b):
    n = len(L)
    y = [0.0 for i in range(n)]
    for i in range(n):
        y[i] = (b[i] - dot(L[i], y)) / L[i][i]
    return y

def back_substitute(U, y):
    n = len(U)
    x = [0.0 for i in range(n)]
    for i in reversed(range(n)):
        x[i] = (y[i] - dot(U[i], x)) / U[i][i]
    return x

def tridiagonal_decompose_and_solve(A, b):
    L, U = tridiagonal_lu(A)
    y = forward_substitute(L, b)
    x = back_substitute(U, y)
    return (L, U, y, x)

# reference: https://www.webpages.uidaho.edu/~barannyk/Teaching/LU_factorization_tridiagonal.pdf
