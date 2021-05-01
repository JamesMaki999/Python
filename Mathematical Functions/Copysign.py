#!/usr/bin/env python3
#Python/Mathematical Functions/Copysign.py
#James Maki
#May 01, 2021

#The copysign() function returns a float value with the absolute value of x but the sign of y.

from math import copysign

def MathFunc(x, y):

    z = copysign(x, y)

    return z

print("Copysign(+ve, -ve): ", MathFunc(1.0, -0.0))
print("Copysign(-ve, +ve): ", MathFunc(-1.0, 0.0))
print("Copysign(+ve, +ve): ", MathFunc(1.0, 0.0))
print("Copysign(+ve, -ve): ", MathFunc(-1.0, -0.0))