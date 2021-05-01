#!/usr/bin/env python3
#Python/Mathematical Functions/Fabs.py
#James Maki
#May 01, 2021

#The fabs() function returns the absolute value, as a float, of the specified expression or a specific number.
#Fabs() removes the negative sign from the given value, if it contains any.

from math import fabs

def MathFunc(x):

    y = fabs(x)

    return y

print("Fabs(+ve): ", MathFunc(5))
print("Fabs(-ve): ", MathFunc(-5))