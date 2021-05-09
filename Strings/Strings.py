#!/usr/bin/env python3
#Python/Strings/Strings.py
#James Maki
#May 04, 2021

#Strings are sequences of characters that are assigned using either 'single quotes' or "double quotes"

#String Assigned to Variable
x = "String"
print(x)

#Multiline Strings | Single Quotes & Double Quotes
x = """
Happy
Birthday
"""
y = '''
Charlie
Brown
'''
print(x + y)

#Looping Through a String
for x in "Python":
    print(x)                # Prints each byte within the string array, one line at a time

#String Length
x = "Python"                # Length of 6
print(len(x))               # The len() function returns the length of a string

#String Check - To check if a certain phrase or character is within a string, use the in keyword
chk = "I'm using Python 3.9.2 to Code"
print("Python" in chk)      # Returns a boolean value of True
#If Statement String Check
if "Python" in chk:
    print("The word 'Python' is in the checked phrase!")
#If Not Statement String Check
if "2.7.3" not in chk:
    print("Python 2.7.3 is not being used for this program!")