##Integration using the Composite trapezoidal rule
##Elect 2017/18
##MAT 351

from math import *
import matplotlib.pyplot as plt
import numpy as np
import random


print("THIS IS A PROGRAM TO DERIVE THE INTEGRAL OF A FUNCTION USING THE COMPOSITE TRAPEZOIDAL RULE")

def trapez(f,a,b,n):
    
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))

    for i in range(1,n):
        s = s + f(a + (i*h))
    print("The integrand of the function given using the composite trapezoidal rule is: ")
    print("\n\t" + str(h*s)) 
    
    ##Draw the graph of the function given with the region shaded
    
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
#    xvalues = linspace(a,b,n)
#    yvalues = [f(y) for y in xvalues]
#    pylab.plot(xvalues, yvalues, "r-o", label="FIND BELOW THE GRAPH OF THE REGION TO BE INTEGRATED")
#    pylab.fill()
#    pylab.legend()
#    pylab.xlabel('x')
   

def g(t):
    return sin(t) 

a = 0
b = (pi/4)
n = 5



x = trapez(g,0,pi/4,5)

print(x)