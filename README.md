# pands-problem-sheet
## WEEKLY TASK SUBMISSIONS
### Shane Austin G00318488

## Week 1:

Create Repositories

## Week 2:

Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared.

``` 
#bmi.py
#Program for calculating BMI
#Author: Shane Austin

weight = int(input("Enter Weight (Kg): "))      #Request Weight
height = int(input("Enter Height (CM): "))      #Request Height

BMI = ((weight)/((height/100)**2))              #Calculate BMI and convert to metres

print ('BMI: {:.1f}' .format(BMI))              #Print BMI to 1 decimal place
``` 

## Week 3:

Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

$ python secondstring.py
Please enter a sentence: The quick brown fox jumps over the lazy dog.
.o zletrv pu o wr cu h

``` 
#secondstring.py
# A program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Shane Austin

inputString = input("Please enter a sentence: ")

#Takes the inputted string reverses by slicing with [::-X] 
#and outputs every second letter with [::2]
#Which equates to [::-2]
newString = inputString[::-2]


print(newString)
```

## Week 4:

Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

``` 
#collatz.py
#A program that takes in an integer and outputs a calculation string
#Author: Shane Austin

num1 = int(input("Please enter a positive integer: "))

while num1 != 1:

    print(num1, end = " ")

    if (num1 % 2) == 1 :
           num1 = ((num1 *3) + 1)

    else:
        num1 = (num1 // 2)

print(num1, end = " ")
```        