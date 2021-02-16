#secondstring.py
# A program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Shane Austin

inputString = input("Please enter a sentence: ")

#Takes the inputted string reverses by slicing with [::-X] and outputs every second letter with [::2]
#Which equates to [::-2]
newString = inputString[::-2]


print(newString)