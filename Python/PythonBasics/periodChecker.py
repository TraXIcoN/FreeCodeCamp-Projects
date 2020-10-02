
# A script to obtain the period, time, date and name of a user.

from getpass import getuser as me
from datetime import *


def my_date():
    dte = datetime.now().date()
    dt_status = dte.strftime("%B %d, %Y")
    return dt_status


def my_time():
    tme = datetime.now().time()
    tm_status = tme.strftime("%H:%M:%S")
    return tm_status


digits = []
for i in range(0, 10, 1):
    digits.append(i)

d_time = my_time()
hr_one = d_time[0]
hr_two = d_time[1]

# Periods of the day
cond1 = int(hr_one) == 0 and int(hr_two) in digits    # Morning
cond2 = int(hr_one) == 1 and int(hr_two) in digits[0:2]    # Morning towards afternoon
cond3 = int(hr_one) == 1 and int(hr_two) in digits[2:6]    # Afternoon
cond4 = int(hr_one) == 1 and int(hr_two) in digits[6:len(digits)]   # Evening
cond5 = int(hr_one) == 2 and int(hr_two) in digits[0:4]   # Evening towards night


def my_period():

    if cond1 or cond2:
        return "Good morning!"
    elif cond3:
        return 'Good afternoon!'
    elif cond4 or cond5:
        return 'Good Evening!'


print("""Hello, {0}! Thank you for running my script.
From your location, the time is {1} and today is {2} \nHence, {3}""".format(me(), my_time(), my_date(), my_period()))

