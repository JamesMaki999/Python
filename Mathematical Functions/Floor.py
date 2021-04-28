#!/usr/bin/env python3
#Python/Mathematical Functions/Floor.py
#James Maki
#April 28, 2021

from math import floor   #Imports the floor() method from the math module

#The floor() method rounds x down to the nearest integer and returns the floor of x

print("Positive, Negative, & Equation")
print("Floor value of Positive Number = ", floor(428.78)) #Positive Floor Value
print("Floor value of Negative Number = ", floor(-28.11)) #Negative Floor Value
print("Floor value of an Equation = ", floor(11 + 15 - 40.21)) #Equation Floor Value

Floor_Tup = (0.98, 2.26, 4.05) #Tuple Declaration
print("\nTuple")
print("Floor value of Tuple Item 1 = ", floor(Floor_Tup[0])) #Tuple Floor Value 1
print("Floor value of Tuple Item 2 = ", floor(Floor_Tup[1])) #Tuple Floor Value 2
print("Floor value of Tuple Item 3 = ", floor(Floor_Tup[2])) #Tuple Floor Value 3

Floor_Lis = [-2.98, 3.65, -8.59] #List Declaration
print("\nList")
print("Floor value of List Item 1 = ", floor(Floor_Lis[0])) #List Floor Value 1
print("Floor value of List Item 2 = ", floor(Floor_Lis[1])) #List Floor Value 2
print("Floor value of List Item 3 = ", floor(Floor_Lis[2])) #List Floor Value 3