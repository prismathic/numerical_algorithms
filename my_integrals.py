# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:42:58 2018

@author: Bamidele
"""
from math import *
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.integrate import quad

print("THIS IS A PROGRAM TO COMPUTE THE INTEGRAL OF A GIVEN FUNCTION BY ANY OF THE METHODS LISTED : ")

##Simple Trapezoidal Rule
def simp_trapez(f,a,b):
    h = (b-a)/2
    print("THE INTEGRAND OF THE FUNCTION GIVEN USING THE SIMPLE TRAPEZOIDAL RULE  WITH a = " + str(a) + ", b = " + str(b) +  " IS: ")
    return h*(f(a) + f(b))
##Riemann Sums
def riemann(f,a,b,n):
    
    print ('TO COMPUTE THE INTEGRAL OF THE GIVEN FUNCTION USING RIEMANN SUMS ')
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
    
    print("THE INTEGRAL OF THE FUNCTION GIVEN, GOTTEN BY COMPUTING THE AVERAGE RIEMANN SUM  WITH a = " + str(a) + ", b = " + str(b) + " WITH NUMBER OF INTERVALS GIVEN TO BE " + str(n) + "  IS : ")    
    
    return ((ls+rs)/2)

##Composite Trapezoidal
def comp_trapez(f,a,b,n):
    
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))

    for i in range(1,n):
        s = s + f(a + (i*h))
    print("THE INTEGRAND OF THE FUNCTION GIVEN USING THE COMPOSITE TRAPEZOIDAL RULE WITH a = " + str(a) + ", b = " + str(b) + " WITH NUMBER OF INTERVALS GIVEN TO BE " + str(n) + " IS: ")
    return (h*s)

##Simpson's rule
def simpson(f,a,b,n):
    h = (b-a)/float(n)
    s = f(a)+f(b)
    for i in range (1,n,2):
        s += (4*f(a+(i*h)))
    for j in range (2,n,2):
        s+=(2*f(a+(j*h)))
    
    print("THE INTEGRAND OF THE FUNCTION GIVEN USING THE COMPOSITE SIMPSON'S RULE  WITH a = " + str(a) + ", b = " + str(b) + " WITH NUMBER OF INTERVALS GIVEN TO BE " + str(n) + "  IS: ")
    return ((h*s)/3)

def plot_graph(f,a,b,n):
#    sub = abs(random.choice(np.linspace(a,b,n)))

    xvalues = np.linspace(a-b,b+b,20)
    yvalues = [f(x) for x in xvalues]
    
    q = min(yvalues) - max(yvalues)
    
    height = max(yvalues) - q
    plt.ylim(q,max(yvalues))
    plt.title('GRAPH PLOT WITH REGION TO BE INTEGRATED SHADED')
    plt.plot(xvalues, yvalues,'r-o')
    
    for y in np.linspace(a, b, n+1):
        plt.axvline(y,0,(f(y)-q)/height)
    return plt.show()

def g(t):
    return ((cos(t))**2)

def true_value(f,a,b):
    return quad(f,a,b)
    

a = 0
b = 2
n = 10

print ("Enter 'A' to compute the integral using Riemman Sums")
print ("Enter 'B' to compute the integral using the Simple Trapezoidal Rule")
print ("Enter 'C' to compute the integral using the Composite Trapezoidal Rule")
print ("Enter 'D' to compute the integral using the Composite Simpson's Rule")
#print ("Enter 'E' to show the combined results using each methods")

user_input = str.upper(input('Choose any of the options above : '))
while True:
    if user_input == 'A':
        x = riemann(g,a,b,n)
        print (x)
        y = true_value(g,a,b)
        print ("THE ERROR IN APPROXIMATION IS : ")
        print (abs(y[0] - x))
        graph = plot_graph(g,a,b,n)
        print (graph)
        break
    elif user_input == 'B':
        x = simp_trapez(g,a,b)
        print (x)
        y = true_value(g,a,b)
        print ("THE ERROR IN APPROXIMATION IS : ")
        print (abs(y[0] - x))
        graph = plot_graph(g,a,b,n=1)
        print (graph)
        break
    elif user_input == 'C':
        x = comp_trapez(g,a,b,n)
        print (x)
        y = true_value(g,a,b)
        print ("THE ERROR IN APPROXIMATION IS : ")
        print (abs(y[0] - x))
        graph = plot_graph(g,a,b,n)
        print (graph)
        break
    elif user_input == 'D':
        x = simpson(g,a,b,n)
        print (x)
        y = true_value(g,a,b)
        print ("THE ERROR IN APPROXIMATION IS : ")
        print (abs(y[0] - x))
        graph = plot_graph(g,a,b,n)
        print (graph)
        break
#    elif user_input == 'E':
#        x_1 = comp_trapez(g,a,b,n)
#        print (x_1)
#        x_2 = simpson(g,a,b,n)
#        print (x_2)
#        y = true_value(g,a,b)
#        print ("THE ERROR IN APPROXIMATION IS : ")
#        print (abs(y[0] - x))
#        graph = plot_graph(g,a,b,n)
#        print (graph)
#        break
    else:
        user_input = str(input('INCORRECT ENTRY!! Please enter from the entries specified : '))
