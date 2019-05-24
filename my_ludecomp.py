##To solve for the solution of a matrix using LU decomposition method
from numpy import *
from numpy.linalg import *

def luresolve(A,b):
    L = A.copy()
    U = A.copy()
    n = A.shape[0]
    L[n-1,n-1] = 1
    for x in range(0,n-1):
        L[x,x] = 1
        for y in range(x+1,n):
            multiplier = U[y,x]/U[x,x]
            U[y]-=(multiplier * U[x])
            L[y,x] = multiplier
            L[x,y] = 0
    print("Matrix A: ")
    print(A)
    print("Matrix B: ")
    print(b)

    print("The Lower Triangular Matrix of the matrix A is: ")
    print (L)
    print("The Upper Triangular Matrix of the matrix A is: ")
    print(U)

    ##Compute for y
    y = dot(inv(L),b)
    print("The value of the matrix y is: ")
    print(y.transpose())
    ##Compute for x
    print("The solution (x) is: ")
    x = dot(inv(U),y)

    return x
    

A = array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]], float)
b = array([-1, 2, 3])

print(luresolve(A,b))
