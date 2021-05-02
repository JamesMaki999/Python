#!/usr/bin/env python3
#Python/Mathematical Functions/FSum.py
#James Maki
#May 01, 2021

"""
The fsum() function calculates and returns the sum of Lists and Tuples (iterates).
TypeError: Occurs when the number argument does not contain a number
"""

from math import fsum           # Importing fsum() function directly from math module

Tup = (10, 20, 12, -40 , 50)    # Tuple Declaration
Lis = [-98, 32, -39, -42 , 15]  # List Declaration

def MathFunc(x):                # MathFunc Declaration

    y = fsum(x)                 # Adds all members of the argument together

    return y                    # Returns summed value back

#Valid FSum Functions
print("fsum of Tuple: ", MathFunc(Tup))
print("fsum of List: ", MathFunc(Lis))
print("fsum of Direct Tuple Items: ", MathFunc((1, 2, 3, 4, 5)))
print("fsum of Direct List Items: ", MathFunc([10, 20, 15, 40, 50]))
print("fsum of Decimal Direct Tuple Items: ", MathFunc((1.2, -5.2, 4.1, 2.3, -1.1)))
print("fsum of Decimal Direct List Items: ", MathFunc([5.2, 4.1, -7.1, 2.7, 8.5]))

#Invalid FSum Functions
print("fsum of Tuple with String arguments: ", MathFunc(('a', 'b', 'c', 'd', 'e')))
print("fsum of List with String arguments: ", MathFunc(['1', '2', 'f', 'g', 't']))