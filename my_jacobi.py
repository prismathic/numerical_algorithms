from numpy import *
from numpy.linalg import *

##a_1_1 = int(input("A(1,1) : "))
##a_1_2 = int(input("A(1,2) : "))
##a_1_3 = int(input("A(1,3) : "))
##a_2_1 = int(input("A(2,1) : "))
##a_2_2 = int(input("A(2,2) : "))
##a_2_3 = int(input("A(2,3) : "))
##a_3_1 = int(input("A(3,1) : "))
##a_3_2 = int(input("A(3,2) : "))
##a_3_3 = int(input("A(3,3) : "))
##
##b_1_1 = int(input("B(1,1) : "))
##b_2_1 = int(input("B(2,1) : "))
##b_3_1 = int(input("B(3,1) : "))

print("THIS IS A PROGRAM TO SOLVE A SYSTEM OF LINEAR EQUATIONS USING THE JACOBI ITERATIVE METHOD")
g_1_1 = int(input("Your initial guess, G(1,1) : "))
g_2_1 = int(input("Your initial guess, G(2,1) : "))
g_3_1 = int(input("Your initial guess, G(3,1) : "))

n = int(input("Maximum number of iterations: "))

def jacobi(A,b,x_init,tol,maxiter):
    diff = tol * 2
    k = 0
    x = x_init.copy()
    x_prev = x_init.copy()
    D = diag(A)
    R = A - diagflat(D)
    while (diff > tol) and k < maxiter:
        for i in range(maxiter):
            x = (b - dot(R,x_prev))/D
        diff = norm(x - x_prev) / norm(x)
        print (x,diff)
        k+=1
        x_prev = x.copy()
    return x,k


A = array([[5, -2, 3],[-3,9,1],[2,-1,-7]])
b = array([-1,2,3])
guess = array([g_1_1, g_2_1, g_3_1])
#A = array([[a_1_1, a_1_2, a_1_3],[a_2_1, a_2_2, a_2_3] , [ a_3_1, a_3_2, a_3_3]])
#b = array([b_1_1, b_2_1, b_3_1])
#guess = array([g_1_1, g_2_1, g_3_1])

tol = 1E-9

x,k = jacobi(A,b,guess,tol,n)

print ("A: ")
print (A)
print ("B: ")
print(b)

print("Your solution (x) is %s, it took %d iterations to achieve this result. "  % (x,k))
print("The condition number of matrix A is %0.4f " % cond(A))
