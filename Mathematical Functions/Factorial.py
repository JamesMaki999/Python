#!/usr/bin/env python3
#Factorial.py
#James Maki
#May 01, 2021

"""
The factorial function finds the factorial of any given number.
DeprecationWarning: Occurs when the user a piece of code has the possibility of deprecating in the future
ValueError: Occurs when argument is a negative integer, positive or negative decimal
TypeError: Occurs when argument is not a number
Factorial is simply the multiplication of all whole numbers from the chosen number (symbol: !) down to 1
n! = n * (n-1)!
"""

from math import factorial

def MathFunc(x):

    y = factorial(x)

    return y

#Valid Factorial Functions
print("Factorial of 1: ", MathFunc(1))      #1! = 1
print("Factorial of 2: ", MathFunc(2))      #2! = 1 * 2
print("Factorial of 3: ", MathFunc(3))      #3! = 1 * 2 * 3
print("Factorial of 4: ", MathFunc(4))      #4! = 1 * 2 * 3 * 4
print("Factorial of 5: ", MathFunc(5))      #5! = 1 * 2 * 3 * 4 * 5
print("Factorial of 6: ", MathFunc(6))      #6! = 1 * 2 * 3 * 4 * 5 * 6

#Invalid Factorial Functions
print("Factorial of -1: ", MathFunc(-1))    #Throws ValueError
print("Factorial of -1.0: ", MathFunc(-1.0))#Throws ValueError
print("Factorial of 1.0: ", MathFunc(1.0))  #Throws DeprecationWarning
