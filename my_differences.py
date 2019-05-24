# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:39:48 2018

@author: Bamidele
"""
import math as math


def forward(f,x,h):
    b = f(x+h)-f(x)
    y = b/h
    return y
def backward(f,x,h):
    b = f(x)-f(x-h)
    y = b/h
    return y
def central(f,x,h):
    b = f(x+h)-f(x-h)
    y = b/(2*h)
    return y
def g(t):
    return math.cos(t)
x = (math.pi)/3
h = 0.1
print("Which of the newton differences methods do you want to use to solve the given function: ")
print("Enter 'A' for the Forward Differences Method")
print("Enter 'B' for the Backward Differences Method")
print("Enter 'C' for the Central Differences Method")

user_input = str.upper(input("Pick a method : "))
while 1:
    if user_input == 'A':
        x = forward(g,x,h)
        print("The derivative of the function by the Newton Forward Difference method is: ")
        print(x)
        break
    elif user_input == 'B':
        x = backward(g,x,h)
        print("The derivative of the function by the Newton Backward Difference method is: ")
        print(x)
        break
    elif user_input == 'C':
        x = central(g,x,h)
        print("The derivative of the function by the Newton Central Difference method is: ")
        print(x)
        break
    else:
        user_input = str(input("The method you picked is not specified, pick a right method from the options given : "))
        
        
    