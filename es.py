#es.py
#A program that reads in a text file and outputs the number of e's it contains
#Author: Shane Austin

#import required for the sys.argv argument
import sys

#Assigning a name to the inputted file using sys.argv to import
filename = sys.argv[1]

#start of the function
def countEs():
    #open the file/read the content and count the "e" instances
    with open (filename) as f:
        content = f.read()
        Es = content.count("e") ## + content.count("E") ##if upper case 'E' required
               
        return Es

#howManyEs = the result of the function
howManyEs = countEs()

#output
print ("There are {} 'E's' in {}".format(howManyEs,filename))