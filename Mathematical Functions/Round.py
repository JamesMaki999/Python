#!/usr/bin/env python3
#Python/Mathematical Functions/Round.py
#James Maki
#April 29, 2021

#The built in round() function rounds x up or down to the nearest integer and returns x

#Round for Integers
print(round(20))

#Round for Floating Point
print(round(20.7))

#Round for an even choice
print(round(5.5))

#Normal Float
print(round(2.665, 2)) #Intentionally rounds to 2.67
print(round(2.675, 2)) #Unintentionally rounds to 2.67

#using decimal.Decimal() to pass the float as a string for precision
from decimal import Decimal
num = Decimal('2.675')
print(round(num, 2))