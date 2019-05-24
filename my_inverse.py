from numpy import *
from numpy.linalg import *


print("THIS IS A PROGRAM TO SOLVE A SYSTEM OF LINEAR EQUATIONS USING THE INVERSE MATRIX METHOD")

def inverse(A,b):
    x = dot(inv(A),b)
    return x

A = array([[5, -2, 3],[-3,9,1],[2,-1,-7]])
b = array([-1,2,3])

x = inverse(A,b)

print ("A: ")
print (A)
print ("B: ")
print(b)

print("Your solution by inverse matrix method is: ")
print(x)
