#bmi.py
#Program for calculating BMI
#Author: Shane Austin

weight = int(input("Enter Weight (Kg): "))      #Request Weight
height = int(input("Enter Height (CM): "))      #Request Height

BMI = ((weight)/((height/100)**2))              #Calculate BMI and convert to metres

print ('BMI: {:.1f}' .format(BMI))              #Print BMI to 1 decimal place    
