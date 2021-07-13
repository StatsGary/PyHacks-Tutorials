# =============================================================================
# Title             PyHacks - Classes  - User Input and String Formatting
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================

welcome = input("Enter name:")
print("Username is: {}".format(welcome))

# String formatting
age = float(input("Enter age (int):"))
txt = "Your age is {} years old."
print(txt.format(age))

# Alter to floating point
txt = "Your age is {:.1f} years and months old"
print(txt.format(age))
