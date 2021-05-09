#!/usr/bin/env python3
#Python/Strings/SlicingStrings.py
#James Maki
#May 04, 2021

"""
String Slicing returns a range of characters by using the slice function
The syntax for slicing strings is: x[str:end]
"""

#String Element Access - In Python, strings are arrays of bytes representing unicode
x = "Python"
print(x[3])                 # Square brackets can be used to access elements of strings

#Slicing Strings
x = "Python Rocks!"
print(x[7:11])              # Grabs the characters from position 7 to position 11

#Slicing Strings From the Start
x = "Python 3.9.2"
print(x[:6])

#Slicing Strings From the End
x = "Python 3.9.2"
print(x[7:])

#String Negative Indexing - Used to start slice from the end of the string
x = "Python Negative Indexing"
print(x[-6:-1])