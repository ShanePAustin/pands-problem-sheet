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
   