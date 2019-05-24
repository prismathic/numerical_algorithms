from numpy import *
from numpy.linalg import *

print("THIS IS A PROGRAM TO SOLVE A SYSTEM OF LINEAR EQUATIONS USING THE CRAMER'S RULE METHOD")

def cramer(A,b):
    a1 = A.copy()
    a2 = A.copy()
    a3 = A.copy()
    a_det = det(A)
    n = A.shape[0]
    k=0

    while k < 3:
        a1[k,0] = b[k]
        a2[k,1] = b[k]
        a3[k,2] = b[k]
        k+=1
    x1_det = det(a1)
    x2_det = det(a2)
    x3_det = det(a3)
    

    x1 = x1_det/a_det
    x2 = x2_det/a_det
    x3 = x3_det/a_det

    x = array([x1,x2,x3])

    return x,x1_det,x2_det,x3_det,a_det

A = array([[5, -2, 3],[-3,9,1],[2,-1,-7]])
b = array([-1,2,3])

x,x1_det,x2_det,x3_det,a_det = cramer(A,b)

print("A: ")
print(A)

print("B: ")
print(b)

print("DELTA A: ")
print(a_det)
print("DELTA X1: ")
print(x1_det)
print("DELTA X2: ")
print(x2_det)
print("DELTA X3: ")
print(x3_det)

print("The solution x is: ")
print(x)


