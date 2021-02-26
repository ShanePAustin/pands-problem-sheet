#squareroot.py
# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Shane Austin


def sqrt (num1):
    #First approximation
    guess = num1
    #test 20 iterations
    for _i in range(20):  
       
        #Newton approximation formula   
        nextGuess = ((guess + num1 /guess)*0.5)
        #Break clause if the guess is close enough for efficiency
        if abs(guess - nextGuess) < 0.000001:
            break
        else:
            guess = nextGuess

    return nextGuess

#set variable to start a loop to avoid incorrect entry
num1 = 0
while (num1 <= 0):
    num1 = float(input("Enter a positive number:"))
    if (num1 <0):
        print("Error: Enter a positive number")
   
approx = (sqrt(num1))

print(round(approx,1))
