#!/usr/bin/env python3
#Python/Flow Control Statements/Elif.py
#James Maki
#May 03, 2021

"""
The Elif statement in Python allows the compiler to test a condition and, depending on the result, execute the code block.
Logical Elif Statement Conditions:
Equals - x == y
Not Equals - x != y
Greater Than - x > y
Greater Than or Equal to - x >= y
Less Than - x < y
Less Than or Equal to - x <= y
"""

x, y = 10, 20               # Variable Declaration

#Equals & Not Equals
if x == y:                  # Equates to False, 10 is not equal to 20
    print("If 'x' is equal to 'y' then this statement will print.")
elif x != y:                # Equates to True, 10 is not equal to 20
    print("Else if 'x' is not equal to 'y' then this statement will print.")
#Greater Than & Greater Than or Equal to
if x > y:                   # Equates to False, 10 is not greater than 20
    print("If 'x' is greater than 'y' then this statement will print.")
elif x >= y:                # Equates to False, 10 is not greater than or equal to 20
    print("Else if 'x' is greater than or equal to 'y' then this statement will print.")
#Less Than & Less Than or Equal to
if x < y:                   # Equates to True, 10 is less than 20
    print("If 'x' is less than 'y' then this statement will print.")
elif x <= y:                # Skipped because the previous if statement executed
    print("Else if 'x' is less than or equal to 'y' then this statement will print.")

#Invalid Elif Statement
if x = y:                   # Syntax error, cannot use an Assignment Operator
    print("'x' equals 'y'")
elif x == y:
print("'x' is equal to 'y'")# Raises an error because Indentation is incredibly important in Python