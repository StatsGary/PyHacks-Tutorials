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
    
# Many exceptions
try:
    print(null_obj)
except NameError:
    print("Please define the object and try again")
except:
    print("It could be something else")
    
    
# Using Else
try:
    print("Hello")
except:
    print("Something's wrong")
else:
    print("All went smoothly")
