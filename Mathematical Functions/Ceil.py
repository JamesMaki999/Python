#!/usr/bin/env python3
#Python/Mathematical Functions/Ceil.py
#James Maki
#April 28, 2021

from math import ceil   #Imports the ceil() method from the math module

#The ceil() method returns the ceiling value, the smallest integer greater than or equal to x

print("Positive, Negative, & Equation")
print("Ceiling value of Positive Number = ", ceil(428.78)) #Positive Ceiling Value
print("Ceiling value of Negative Number = ", ceil(-28.11)) #Negative Ceiling Value
print("Ceiling value of an Equation = ", ceil(19 + 18 - 11.21)) #Equation Ceiling Value

Ceil_Tup = (1.98, 0.26, 1.05) #Tuple Declaration
print("\nTuple")
print("Ceiling value of Tuple Item 1 = ", ceil(Ceil_Tup[0])) #Tuple Ceiling Value 1
print("Ceiling value of Tuple Item 2 = ", ceil(Ceil_Tup[1])) #Tuple Ceiling Value 2
print("Ceiling value of Tuple Item 3 = ", ceil(Ceil_Tup[2])) #Tuple Ceiling Value 3

Ceil_Lis = [-1.98, 2.65, -6.59] #List Declaration
print("\nList")
print("Ceiling value of List Item 1 = ", ceil(Ceil_Lis[0])) #List Ceiling Value 1
print("Ceiling value of List Item 2 = ", ceil(Ceil_Lis[1])) #List Ceiling Value 2
print("Ceiling value of List Item 3 = ", ceil(Ceil_Lis[2])) #List Ceiling Value 3