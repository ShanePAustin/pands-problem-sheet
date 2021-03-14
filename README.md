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
```python
weight = int(input("Enter Weight (Kg): "))      
height = int(input("Enter Height (CM): "))      

BMI = ((weight)/((height/100)**2))              

print ('BMI: {:.1f}' .format(BMI))
``` 
#### Understanding:

* The first two lines of the code request and inputted integer from the user and defines them as
weight and height. [1]

* The next line processes the BMI calculation BMI = kg/m2. [2]

* The last line prints the result of the calculation and formats it to 1 decimal place. [3]

#### References:

1) https://www.w3schools.com/python/ref_func_input.asp

2) https://www.calculator.net/bmi-calculator.html

3) https://stackoverflow.com/questions/3400965/getting-only-1-decimal-place

## Week 3:

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*

*$ python secondstring.py*

*Please enter a sentence: The quick brown fox jumps over the lazy dog.*

*.o zletrv pu o wr cu h*

#### Code:
##### secondstring.py
```python 
inputString = input("Please enter a sentence: ")

newString = inputString[::-2]

print(newString)
```
#### Understanding:

* Requests a input string from the user

* Takes the inputted string reverses by slicing with [::-1] and outputs every second letter with [::2]
Which equates to [::-2] [1][2]

* Then prints the new string

#### References:

1) https://www.w3schools.com/python/ref_func_slice.asp

2) https://www.w3schools.com/python/python_howto_reverse_string.asp

## Week 4:

*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.*

*At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one*

*Have the program end if the current value is one.*

#### Code:
##### collatz.py
```python 
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

* Defines num1 as an inputted variable from the user

* It carries out the loop if the number does not equal 1 using 'while' [1]

* The value gets printed to the line at the start of every loop, and carries out one of two calculations: [3]

* If the number is odd (the remainder the number divded by 2 equals 1) the number is multiplied by 3 and 1 is added. Using an 'If' statement [2]

* If the number is even it is divided by 2. Using the 'Else' statement [2]

* The respective calcutlations are carried out and printed to the string until the number gets down to 1 and it stops the loop

* The final string is then printed

#### References:

1) https://www.w3schools.com/python/python_while_loops.asp

2) https://www.w3schools.com/python/python_conditions.asp

3) https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

## Week 5:

*Write a program that outputs whether or not today is a weekday.*


#### Code:
##### weekday.py
```python 
import datetime

time = datetime.datetime.now()
today = (time.strftime("%A"))

if (today == 'Saturday' or today == 'Sunday'):
    print("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")

```      
#### Understanding:

* Imports the datetime module and set the current date and time within the program (time = datetime.datetime.now()) [1]

* %A references the full word for the weekday

* 'If' argument for when the actual day is Saturday or Sunday [2][3]

* 'Else' for all other days

* The program prints the required output for the specific instance

#### References:  

1) https://www.w3schools.com/python/python_datetime.asp

2) https://www.geeksforgeeks.org/difference-operator-python/

3) https://www.w3schools.com/python/python_conditions.asp

## Week 6:

*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*


#### Code:
##### squareroot.py
```python 
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

* Isaac Newton devised a clever method to easily approximate the square root without having to use a calculator that has the square root function. His method consists of making an educated guess and then entering it into his simple equation. You repeatedly take your answer and enter it in his equation until the correct square root is obtained. √ N ≈ ½(N/A + A) (shown in the school for champions link) [1]

* When the function starts by taking in the inputted from the user and defines it as 'guess' to be the first approximation.

* It starts a 'for loop' for an assigned 20 iterations. (this seemed to be more than enough to get an accurate approximation) [2]

* It then starts the Newton formula with the requested number and the first approximation. It takes the result and redfines the output to be the guess in the next iteration.

* It will keep doing this loop 20 times or until the result is close enough, (the difference between the current guess and the previous iteration is less than 0.00001) it will then break the loop and return the result. (It will most likely work with only one of these break clauses but I included both to maintain efficiency and prevent an infinite loop). [3]

* At the start num1 is set to = 0 so it won't run until a positive integer is input, if '0' or a negative number is inputted it will request a positive number again.

* The program then runs the function with the defined input.

* It prints the result and rounds to 1 decimal place.

#### References:  

1) https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDg9h2j7QuU

2) https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method

3) https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

## Week 7:

*Write a program that reads in a text file and outputs the number of e's it contains.*

*The program should take the filename from an argument on the command line.*


#### Code:
##### es.py
```python 
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

* import sys and sys.argv[] lets you import a file to be processed within the command line, here I have defined the imported file to be called 'filename' [3]

* The function is defined as countEs which opens the file, reads the content and counts the instances of 'e' within the text and returns the result. [1] [2]

* The result of the function is defined as howManyEs and outputted for the user.

#### References:  

1) https://www.w3schools.com/python/ref_file_read.asp

2) https://www.programiz.com/python-programming/methods/string/count

3) https://bham-carpentries.github.io/2018-07-26-python_python-novice-inflammation/10-cmdline/index.html

## Week 8:

*Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes..*

#### Code:
##### plotTask.py
```python 
import matplotlib.pyplot as plt
import numpy as np

lowRange = 0
highRange = 4
step = (highRange*10)+1

ax = plt.axes()
plt.ylim(-2,70)

xpoints = np.linspace(lowRange,highRange,step)

fx = xpoints
gx = xpoints**2
hx = xpoints**3

plt.plot(xpoints, fx,label = "$f(x)= x$", color="firebrick", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, gx,label = "$g(x)= x^{2}$", color="royalblue", linewidth = 2, marker = "o", markevery = 10)
plt.plot(xpoints, hx, label = "$h(x)= x^{3}$", color="forestgreen", linewidth = 2, marker = "o", markevery = 10)

plt.title ("Values of $x$, $x^{}$, and $x^{}$ in the range {}-{}".format(2,3,lowRange,highRange))
plt.xlabel("$x$")
plt.ylabel("$x^{n}$")
plt.legend()

plt.grid(linestyle ="dashed")
ax.set_facecolor("lightgrey")

plt.savefig("plotTask.png")
```      
#### Understanding:

![alt text](https://github.com/ShanePAustin/pands-problem-sheet/blob/main/plotTest.png "First Plot")

![alt text](https://github.com/ShanePAustin/pands-problem-sheet/blob/main/plotTask.png "Final Plot")
#### References:  

1) 

2) 

3) 
