# =============================================================================
# Title             PyHacks - Classes  - Dates
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:

#-----------------------PYTHON DATES----------------------------------------
import datetime 

def seperate_returns(length_pad=60):
    # Get name of month
    print(str("-" * length_pad))

# Return the time now
today_datetime = datetime.datetime.now()
print(today_datetime)
# Return the year and name of weekday
print(today_datetime.year)
print(today_datetime.strftime("%A"))

#-----------------------CREATING DATE OBJECTS-------------------------------

custom_date = datetime.datetime(2021,5,22)
print(custom_date)
print(type(custom_date))

#-----------------------FORMATTING DATE OBJECTS-----------------------------
cdate = datetime.datetime(2015,10,27)

seperate_returns()
print(cdate.strftime("%B"))

# Get weekday short version
print(cdate.strftime("%a"))

# Get weekday long
print(cdate.strftime("%A"))

# Weekday as a number 0-6, 0 is Sunday
print(cdate.strftime("%w"))

# Get day of the month
print(cdate.strftime("%d"))

# Get month name short ver
print(cdate.strftime("%b"))

# Month name full version
print(cdate.strftime("%B"))

# Month as int
print(cdate.strftime("%m"))

# Month as int
print(cdate.strftime("%m"))