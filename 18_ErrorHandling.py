# =============================================================================
# Title             PyHacks - Classes  - Error Handling
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================
T#he try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(null_obj)
except:
    print("Initialise the object")
    
# ----------------------------Many exceptions --------------------------------
try:
    print(null_obj)
except NameError:
    print("Please define the object and try again")
except:
    print("It could be something else")
    
       
# ----------------------------Using Else  ------------------------------------
try:
    print("Hello")
except:
    print("Something's wrong")
else:
    print("All went smoothly")
    
# ----------------------------Using Finally-----------------------------------

try: 
    print("I am trying to do this bit of code!")
except:
    print("Oh no, something untoward happened!")
finally:
    print("Do something at the end of the code. Things like garbage collection, cleaning environment, normally go here.")

# ----------------------------Custom Exception Messages-----------------------

# Raise an exception
val = -1
if val < 0:
    raise Exception("This cannot contain numbers below zero")
#The raise keyword is used to raise an exception.
#You can define what kind of error to raise, and the text to print to the user.

string = "This will error, as it is a string and not an integer (number)"
if not type(string) is int:
    raise TypeError("Only numbers I am afraid!")