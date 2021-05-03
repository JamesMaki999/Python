#!/usr/bin/env python3
#Python/Mathematical Functions/Frexp.py
#James Maki
#May 03, 2021

"""
The frexp() function returns the mantissa and exponent of x, as pair (m, e).
M is always returned a decimal, while e is always returned an integer
The formula for frexp() funciton is: Number = m * 2**e
TypeError: Occurs when argument is not a number
"""

from math import frexp          # Importing frexp() function directly from math module

Tup = (10, 20, 12, -40 , 50)    # Tuple Declaration
Lis = [-98, 32, -39, -42 , 15]  # List Declaration

def MathFunc(x):                # MathFunc Declaration

    y = frexp(x)                # Number = m * 2**e

    return y                    # Returns summed value back

#Valid frexp Functions
print("frexp of Positive Integer: ", MathFunc(2))
print("frexp of Negative Integer: ", MathFunc(-3))
print("frexp of Positive Decimal: ", MathFunc(4.6))
print("frexp of Positive Decimal: ", MathFunc(-3.2))
print("frexp of Direct Tuple Items: ", MathFunc(Tup[3]))
print("frexp of Direct List Items: ", MathFunc(Lis[1]))
print("frexp of an Equation: ", MathFunc(17 + 3 - 14))

#Invalid frexp Functions
print("frexp of Tuple with String arguments: ", MathFunc(('2.73')))