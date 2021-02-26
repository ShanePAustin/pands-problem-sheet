#weekday.py
#A program that outputs whether or not today is a weekday.
#Author: Shane Austin

import datetime
#sets the time to current date and time
time = datetime.datetime.now()

#%A references full word for the weekday
today = (time.strftime("%A"))


if (today == 'Saturday' or today == 'Sunday'):
    print("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")
