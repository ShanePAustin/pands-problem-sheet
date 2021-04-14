#squareroot.py
# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Shane Austin


def sqrt (num1):
    #First approximation
    guess = num1
    #Loop until condition is met
    while True:  
       
        #Newton approximation formula   
        nextGuess = ((guess + num1 /guess)*0.5)
        #Break clause if the guess is close enough for efficiency
        if abs(guess - nextGuess) < 0.000001:
            break
        #assigning the nextGuess for the next iteration 
        else:
            guess = nextGuess

    return nextGuess

#set variable to start a loop to avoid incorrect entry
num1 = 0
while (num1 <= 0):
    num1 = float(input("Enter a positive number:"))
    if (num1 <0):
        print("Error: Enter a positive number")

#run the function 
approx = (sqrt(num1))

#Print the result and round to 1dp
print(round(approx,1))
