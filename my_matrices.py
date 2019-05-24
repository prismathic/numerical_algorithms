# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:10:52 2018

@author: Bamidele
"""
from numpy import *
from numpy.linalg import *

##Inverse Method
def inverse(A,b):
    x = dot(inv(A),b)
    print ("\nTHE INVERSE OF A IS : ")
    print(inv(A))
    print("\nTHE SOLUTION (X) OF THE MATRIX IS : ")
    return x

##Crammer's Rule
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
    print("\nDELTA A: ")
    print(a_det)
    print("\nDELTA X1: ")
    print(x1_det)
    print("\nDELTA X2: ")
    print(x2_det)
    print("\nDELTA X3: ")
    print(x3_det)
    
    print("\nTHE SOLUTION (X) OF THE MATRIX IS : ")

    return x

##Gaussian Elimination
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
    print("\nAFTER THE FORWARD ELIMINATION, THE RESULT IS: ")
    print("\nA: ")
    print (C)
    print("\nb: ")
    print (b_new)
    
    
    print("\nTHE SOLUTION (X) OF THE MATRIX IS : ")
   

    return x

##LU Decomposition
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
#    print("Matrix A: ")
#    print(A)
#    print("Matrix B: ")
#    print(b)

    print("\nTHE LOWER TRIANGULAR MATRIX OF THE MATRIX A IS: ")
    print (L)
    print("\nTHE UPPER TRIANGULAR MATRIX OF THE MATRIX A IS: ")
    print(U)

    ##Compute for y
    y = dot(inv(L),b)
    print("\nTHE VALUE OF THE MATRIX Y IS: ")
    print(y.transpose())
    ##Compute for x
    print("\nTHE SOLUTION (X) IS: ")
    x = dot(inv(U),y)

    return x

##Jacobi Iterative
def jacobi(A,b,x_init,tol,maxiter):
    diff = tol * 2
    k = 0
    x = x_init.copy()
    x_prev = x_init.copy()
    D = diag(A)
    R = A - diagflat(D)
    print("\nITERATIONS...")
    while (diff > tol) and k < maxiter:
        for i in range(maxiter):
            x = (b - dot(R,x_prev))/D
        diff = norm(x - x_prev) / norm(x)
        print (x,diff)
        k+=1
        x_prev = x.copy()
    print("\nAFTER " + str(k) + " ITERATIONS, THE SOLUTION (X) OF THE MATRIX IS : ")
    return x 

A = array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]], float)
b = array([-1,2,3], float)



print("THIS IS A PROGRAM TO DETERMINE THE SOLUTION MATRIX TO A 3 X 3 SQUARE MATRIX USING EITHER DIRECT OR ITERATIVE METHODS")

while True:
    
    print ("\nEnter 'A' to derive the solution using the inverse method")
    print ("Enter 'B' to derive the solution using Cramer's Rule")
    print ("Enter 'C' to derive the solution by Gaussian Elimination")
    print ("Enter 'D' to derive the solution by LU Decomposition")
    print ("Enter 'E' to derive the solution through the Jacobi Iterative method")
    print ("Enter 'X' to end the program")
    
    
    user_input = str.upper(input("Enter any of the options above : "))
    
    if user_input == 'A':
        print("TO SOLVE THE SYSTEM OF LINEAR EQUATIONS USING THE INVERSE METHOD")
        print ("A : ")
        print(A)
        print ("b : ")
        print(b)
        x = inverse(A,b)
        print(x)
    elif user_input == 'B':
        print("TO SOLVE THE SYSTEM OF LINEAR EQUATIONS USING CRAMER'S RULE")
        print ("A : ")
        print(A)
        print ("b : ")
        print (b)
        x = cramer(A,b)
        print(x)
    elif user_input == 'C':
        print("TO SOLVE THE SYSTEM OF LINEAR EQUATIONS USING GAUSSIAN ELIMINATION")
        print ("A : ")
        print(A)
        print ("b : ")
        print (b)
        x = gauss(A,b)
        print(x)
    elif user_input == 'D':
        print("TO SOLVE THE SYSTEM OF LINEAR EQUATIONS USING LU DECOMPOSITION")
        print ("A : ")
        print(A)
        print ("b : ")
        print (b)
        x = luresolve(A,b)
        print(x)
    elif user_input == 'E':
        print("TO SOLVE THE SYSTEM OF LINEAR EQUATIONS USING JACOBI ITERATION")
        x_1 = int(input("YOUR INITIAL GUESS, G(1,1) : "))
        x_2 = int(input("YOUR INITIAL GUESS, G(2,1) : "))
        x_3 = int(input("YOUR INITIAL GUESS, G(3,1) : "))
        n = int(input("MAXIMUM NUMBER OF ITERATIONS (In Case it does not converge): "))
        
        guess = array([x_1, x_2, x_3])
        tol = 1E-9
        
        print ("A : ")
        print(A)
        print ("b : ")
        print (b)
        x = jacobi(A,b,guess,tol,n)
        print(x)
    elif user_input == 'X':
        break
    else:
        print('INCORRECT ENTRY!! Please enter from the entries specified : ')
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    