#!/usr/bin/env python3
#Python/Mathematical Functions/FMod.py
#James Maki
#May 01, 2021

"""
The fmod() function returns the remainder (modulo) of x/y
ValueError: Occurs when both x and y = 0, or when only y = 0
TypeError: Occurs when x or y are not a numeric value
"""

from math import fmod

def MathFunc(x, y):

    z = fmod(x, y)

    return z

#Valid FMod Functions
print("fmod(20, 4): ", MathFunc(20, 4))
print("fmod(20, 3): ", MathFunc(20, 3))
print("fmod(-10, 3): ", MathFunc(-10, 3))

#Invalid FMod Functions
print("fmod(0, 0): ", MathFunc(0, 0))
print("fmod(0, 0): ", MathFunc(True, "4"))