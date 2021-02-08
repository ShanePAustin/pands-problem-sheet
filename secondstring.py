#secondstring.py
# A program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Shane Austin

inputString = input("Please enter a sentence: ")

#Takes the inputted string reverses by slicing with [::-1] and outputs every second letter with [::2]
newString = inputString[::-1]
alternateString = newString[::2]

print(alternateString)