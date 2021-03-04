##### pands-problem-sheet
# WEEKLY TASK SUBMISSIONS
### Programming and Scripting 52167

### Shane Austin G00318488

## Week 1:

Create Repositories

## Week 2:

*Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py*

*The inputs are the person's height in centimetres and weight in kilograms.*

*The output  is their weight divided by their height in metres squared.*

#### Code:
##### BMI.py
``` 
weight = int(input("Enter Weight (Kg): "))      
height = int(input("Enter Height (CM): "))      

BMI = ((weight)/((height/100)**2))              

print ('BMI: {:.1f}' .format(BMI))
``` 
#### Understanding:

The first two lines of the code request and inputted integer from the user and defines them as
weight and height.

The next line processes the BMI calculation BMI = kg/m2.

The last line prints the result of the calculation and formats it to 1 decimal place

#### References:

https://www.w3schools.com/python/ref_func_input.asp

https://www.calculator.net/bmi-calculator.html

https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place

## Week 3:

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*

*$ python secondstring.py*

*Please enter a sentence: The quick brown fox jumps over the lazy dog.*

*.o zletrv pu o wr cu h*

#### Code:
##### secondstring.py
``` 
inputString = input("Please enter a sentence: ")

newString = inputString[::-2]

print(newString)
```
#### Understanding:

Requests a input string from the user

Takes the inputted string reverses by slicing with [::-1] and outputs every second letter with [::2]
Which equates to [::-2]

Then prints the new string

#### References:

https://www.w3schools.com/python/ref_func_slice.asp

https://www.w3schools.com/python/python_howto_reverse_string.asp

## Week 4:

*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.*

*At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one*

*Have the program end if the current value is one.*

#### Code:
##### collatz.py
``` 
num1 = int(input("Please enter a positive integer: "))

while num1 != 1:

    print(num1, end = " ")

    if (num1 % 2) == 1 :
           num1 = ((num1 *3) + 1)

    else:
        num1 = (num1 // 2)

print(num1, end = " ")
```      
#### Understanding:

Defines num1 as an inputted variable from the user

It carries out the loop if the number does not equal 1 using 'while'

The value gets printed to the line at the start of every loop, and carries out one of two calculations:

If the number is odd (the remainder the number divded by 2 equals 1) the number is multiplied by 3 and 1 is added. Using an 'If' statement

If the number is even it is divided by 2. Using the 'Else' statement

The respective calcutlations are carried out and printed to the string until the number gets down to 1 and it stops the loop

The final string is then printed

#### References:

https://www.w3schools.com/python/python_while_loops.asp

https://www.w3schools.com/python/python_conditions.asp

https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

## Week 5:

*Write a program that outputs whether or not today is a weekday.*


#### Code:
##### weekday.py
``` 
import datetime

time = datetime.datetime.now()
today = (time.strftime("%A"))

if (today == 'Saturday' or today == 'Sunday'):
    print("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")

```      
#### Understanding:

Imports the datetime module and set the current date and time within the program (time = datetime.datetime.now())

%A references the full word for the weekday

'If' argument for when the actual day is Saturday or Sunday

'Else' for all other days

The program prints the required output for the specific instance

#### References:  

https://www.w3schools.com/python/python_datetime.asp

https://www.geeksforgeeks.org/difference-operator-python/

https://www.w3schools.com/python/python_conditions.asp

## Week 6:

*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*


#### Code:
##### squareroot.py
``` 
def sqrt (num1):
    guess = num1
    for _i in range(20):  
         
        nextGuess = ((guess + num1 /guess)*0.5)
        if abs(guess - nextGuess) < 0.000001:
            break
        else:
            guess = nextGuess

    return nextGuess

num1 = 0
while (num1 <= 0):
    num1 = float(input("Enter a positive number:"))
    if (num1 <0):
        print("Error: Enter a positive number")
   
approx = (sqrt(num1))

print(round(approx,1))
```      
#### Understanding:

#### References:  

https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDg9h2j7QuU

https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method

https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

## Week 7:

*Write a program that reads in a text file and outputs the number of e's it contains.*


#### Code:
##### es.py
``` 
import sys

filename = sys.argv[1]

def countEs():

    with open (filename) as f:
        content = f.read()
        Es = content.count("e")
       
        return Es

howManyEs = countEs()
print ("There are {} 'E's' in {}".format(howManyEs,filename))
```      
#### Understanding:

#### References:  

https://www.w3schools.com/python/ref_file_read.asp

https://www.programiz.com/python-programming/methods/string/count

https://bham-carpentries.github.io/2018-07-26-python_python-novice-inflammation/10-cmdline/index.html
