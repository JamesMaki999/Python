#!/usr/bin/env python3
#Python/Strings/EscapeCharacters.py
#James Maki
#May 09, 2021

"""
Escape Characters in Python are executed by using a backslash (\), followed by the character you wish to input
Escape Characters:
Single Quote (\' \')
Double Quote (\" \")
Backslash (\\)
New Line (\n)
Carriage Return (\r)
Tab (\t)
Backspace (\b)
Form Feed (\f)
Octal Value (\ooo)
Hex Value (\ xhh)       # Ignore the space, without it this example would error the entire comment out
"""

#Invalid Escape Character - Double Quotes
#print("I'm James, the so-called "Destroyer of Code", Maki")     # Syntax Error

#Valid Escape Character - Double Quotes
print("I'm James, the so-called \"Destroyer of Code\", Maki")

#Escape Character - Single Quotes
print('It\'s fine.')

#Escape Character - Backslash
print("This is how you print a single \\ (backslash)")

#Escape Character - New Line
print("Python\nProgrammer")

#Escape Character - Carriage Return
print("Python\rProgrammer")

#Escape Character - Tab
print("Python\tProgrammer")

#Escape Character - Backspace
print("Python \bProgrammer")    # Removes one space

#Escape Character - Form Feed
print("Python\fProgrammer")

#Escape Character - Octal Value
print("\120\171\164\150\157\156")

#Escape Character - Hex Value
print("\x50\x79\x74\x68\x6f\x6e")