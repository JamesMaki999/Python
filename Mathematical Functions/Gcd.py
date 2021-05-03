#!/usr/bin/env python3
#Python/Mathematical Functions/Gcd.py
#James Maki
#May 03, 2021

"""
The gcd() function returns the greatest common divisor of two given arguments.
M is always returned a decimal, while e is always returned an integer
The formula for gcd() funciton is: gcd(x, y)
TypeError: Occurs if the X or Y argument is a Decimal, or If the X value or Y argument is not a number
"""

from math import gcd            # Importing gcd() function directly from math module

Tup = (10, 20, 12, -40 , 50)    # Tuple Declaration
Lis = [-98, 32, -39, -42 , 15]  # List Declaration

def MathFunc(x, y):             # MathFunc Declaration

    z = gcd(x, y)

    return z                    # Returns divisor value

#Valid gcd Functions
print("gcd of Positive Integer: ", MathFunc(2, 3))
print("gcd of Negative Integer: ", MathFunc(-2, 3))
print("gcd of Non-Zero and Zero: ", MathFunc(4, 0))
print("gcd of Zero and Non-Zero: ", MathFunc(0, 2))
print("gcd of Zero: ", MathFunc(0, 0))
print("gcd of Direct Tuple Items: ", MathFunc(Tup[0], Tup[2]))
print("gcd of Direct List Items: ", MathFunc(Lis[1], Lis[2]))
print("gcd of an Equation: ", MathFunc(17 + 3 - 14, 4 + 2))

#Invalid gcd Functions
print("gcd of Positive Decimal: ", MathFunc(1.5, 4.2))
print("gcd of Tuple with String arguments: ", MathFunc(('2.73', '3')))