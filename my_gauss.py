from numpy import *
from numpy.linalg import *

print("THIS IS A PROGRAM TO SOLVE A SYSTEM OF LINEAR EQUATIONS USING THE GAUSSIAN ELIMINATION METHOD")

def gauss(A,b):
    A_new  = A.copy()
    b= b.transpose()
    C = column_stack((A_new,b))
    if C[1,0] != 0:
        mult_1 = C[1,0]/C[0,0]
        C[1] = C[1] - (mult_1 * C[0])
    if C[2,0] !=0:
        mult_2 = C[2,0]/C[0,0]
        C[2] = C[2] - (mult_2 * C[0])
        if C[2,1] !=0:
            mult_3 = C[2,1]/C[1,1]
            C[2] = C[2] - (mult_3 * C[1])

    b_new = C[...,3]
    C = delete(C, 3, axis=1)
    x = dot(inv(C),b_new)
    print("After the forward elimination, the result is: ")
    print("A: ")
    print (C)
    print("b: ")
    print (b_new)

   

    return x


A = array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]], float)
b = array([-1,2,3], float)

x = gauss(A,b)

print("A: ")
print(A)

print("b: ")
print(b)

print("X: ")
print(x)
