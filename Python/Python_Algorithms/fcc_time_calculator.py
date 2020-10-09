#! python 3

"""
fcc_time_calculator.py - return time/day give original time/day and delta time
"""

from datetime import timedelta, datetime


def get_time(hrs_mins):
    hrs, mins = [x for x in hrs_mins.split(":")]
    return timedelta(hours = int(hrs), minutes = int(mins))

def _12_to_24(hrs_mins_ampm):
    temp_time = datetime.strptime(hrs_mins_ampm, "%I:%M %p")
    return datetime.strftime(temp_time, "%H:%M")

def _24_to_12(hrs_mins):
    temp_time = datetime.strptime(hrs_mins, "%H:%M")
    return datetime.strftime(temp_time, "%I:%M %p")

def add_time(old_time, change, *day):
    day_num = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3,
            "friday":4, "saturday":5, "sunday":6}
    num_day = {n:d for d,n in day_num.items()}

    old_time_24hr = _12_to_24(old_time)

    time_diff = get_time(old_time_24hr) + get_time(change)
    
    hrs = time_diff.seconds//3600
    mins = time_diff.seconds%3600//60

    hours_diff = _24_to_12(f"{hrs}:{mins}")
    days_diff = time_diff.days


    new_day = ""
    if day:
        new_day = (day_num[day[0].lower()] + days_diff)//7
        new_day = f", {num_day[new_day].capitalize()}"
        
    day_change = f" ({days_diff} days later)" if days_diff > 1 else \
                 " (next day)" if days_diff else ""
    
    updated_time = hours_diff + new_day + day_change
    print(updated_time)
    print("\n")
    return updated_time


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
