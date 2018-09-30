from pprint import pprint
from numpy import dot

def lu(A):
    n = len(A)
    L = [[(1.0 if i == j else 0.0) for i in range(n)] for j in range(n)]
    U = [[0.0] * n for i in range(n)]
    for j in range(n):
        for i in range(j+1):
            U[i][j] = A[i][j] - sum(U[k][j] * L[i][k] for k in range(i))
        for i in range(j, n):
            L[i][j] = (A[i][j] - sum(U[k][j] * L[i][k] for k in range(j))) / U[j][j]
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

def decompose_and_solve(A, b):
    L, U = lu(A)
    y = forward_substitute(L, b)
    x = back_substitute(U, y)
    return (L, U, y, x)
