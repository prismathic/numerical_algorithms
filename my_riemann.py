##To solve for the integrand of a function using the riemann integral

from math import *
import matplotlib.pyplot as plt
import numpy as np
import random

print("THIS IS A PROGRAM TO DERIVE THE INTEGRAL OF A FUNCTION USING THE RIEMANN INTEGRALS")

def riemann(f,a,b,n):
    h = (b-a)/float(n)
    ls = f(a)
    rs = f(b)

    for i in range(1,n):
        ls= ls + f(a+(i*h))
        rs= rs + f(a-(i*h))
    ls = h*ls
    rs = h*rs

    # print("THE FUNCTION GIVEN: ")
    # print(f)

    print("LEFT RIEMANN SUM: ")
    print(ls)

    print("RIGHT RIEMANN SUM: ")
    print(rs)
    
    print("The Average riemann sum is: ")    
    
    print ((ls+rs)/2)

    sub = abs(random.choice(np.linspace(a,b,n)))

    xvalues = np.linspace(a-sub,b+sub,20)
    yvalues = [f(x) for x in xvalues]
    
    q = min(yvalues) - abs(random.choice(yvalues))
    
    height = max(yvalues) - q
    plt.ylim(q,max(yvalues))
    plt.title('Graph Plot with region to be integrated shaded')
    plt.plot(xvalues, yvalues,'r-o')
    
    for y in np.linspace(a, b, n+1):
        plt.axvline(y,0,(f(y)-q)/height)
    return plt.show()

def g(t):
    return cosh(t)

a = 0
b = 2
n = 6
x = riemann(g,a,b,n)
print(x)


