#collatz.py
#A program that takes in an integer and outputs a calculation string
#Author: Shane Austin

num1 = int(input("Please enter a positive integer: "))

#do the loop if the number does not = 1
while num1 != 1:
    #print the calculation to the string for each iteration
    print(num1, end = " ")

    #the first conditon of the formula
    if (num1 % 2) == 1 :
           num1 = ((num1 *3) + 1)

    #the second condition of the formula
    else:
        num1 = (num1 // 2)

#print the full string with 1 at the end as it doesn't go through the loop
print(num1, end = " ")





