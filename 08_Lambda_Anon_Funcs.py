# =============================================================================
# Title             PyHacks - Lambda Functions
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      07/07/2021
# =============================================================================

# A lambda function is a small anonymous function. 
# This function can take any number of arguments, 
# but can only have one expression.


square = lambda val : val ** 2
print(square(3))

summer = lambda val1, val2, val3: val1 + val2 + val3
print(summer(5, 61, 20))