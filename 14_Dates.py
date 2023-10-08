# =============================================================================
# Title             PyHacks - Classes  - Dates
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================


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
seperate_returns()
#-----------------------CREATING DATE OBJECTS-------------------------------

custom_date = datetime.datetime(2021,5,22)
print(custom_date)
print(type(custom_date))
seperate_returns()
#-----------------------FORMATTING DATE OBJECTS-----------------------------
cdate = datetime.datetime(2015,10,27)

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

# =============================================================================
# # Full list of methods and formatting options
# Format	Description	Example
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month 01-31	31
# %b	Month name, short version	Dec
# %B	Month name, full version	December
# %m	Month as a number 01-12	12
# %y	Year, short version, without century	18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	5
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	8
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	1
# =============================================================================
