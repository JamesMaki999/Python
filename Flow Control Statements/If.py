#!/usr/bin/env python3
#Python/Flow Control Statements/If.py
#James Maki
#May 03, 2021

"""
The If statement in Python allows the compiler to test a condition and, depending on the result, execute the code block.
Logical If Statement Conditions:
Equals - x == y
Not Equals - x != y
Greater Than - x > y
Greater Than or Equal to - x >= y
Less Than - x < y
Less Than or Equal to - x <= y
"""

x, y = 10, 20               # Variable Declaration

#Equals
if x == y:                  # Equates to False, 10 is not equal to 20
    print("If 'x' is equal to 'y' then this statement will print.")
#Not Equals
if x != y:                  # Equates to True, 10 is not equal to 20
    print("If 'x' is not equal to 'y' then this statement will print.")
#Greater Than
if x > y:                  # Equates to False, 10 is not greater than 20
    print("If 'x' is greater than 'y' then this statement will print.")
#Greater Than or Equal to
if x >= y:                  # Equates to False, 10 is not greater than or equal to 20
    print("If 'x' is greater than or equal to 'y' then this statement will print.")
#Less Than
if x < y:                  # Equates to True, 10 is less than 20
    print("If 'x' is less than 'y' then this statement will print.")
#Less Than or Equal to
if x <= y:                  # Equates to True, 10 is less than or equal to 20
    print("If 'x' is less than or equal to 'y' then this statement will print.")

#Invalid If Statement
if x = y:                   # Syntax error, cannot use an Assignment Operator
    print("'x' equals 'y'")
if x == y:
print("'x' is equal to 'y'")# Raises an error because Indentation is incredibly important in Python
