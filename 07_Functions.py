# =============================================================================
# Title             PyHacks - Putting the Fun in Functions
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      07/07/2021
# =============================================================================


# ------------- Create basic calculator function ------------------#
# The operator function has a default parameter
def calc(val1, val2, operator='+'):
    if operator == '+':
        result = val1 + val2
    elif operator == '-':
        result = val1 - val2
    elif operator == '*':
        result = val1 * val2
    elif operator == '/':
        result = val1 / val2
    elif operator == '**':
        result = val1 ** val2
    print(result)
    
# Calling and using our calculator

calc(10,20, operator="+")
calc(10,2, operator="**")
calc(10,50)

# ------------- Dealing with unknown args --------------------------#
def calc(*val, operator='+'):
    hold_vals = []
    for arg in val:
        hold_vals.append(arg)
    if operator == '+':
        result = sum(hold_vals)
    return(result)

# Call the unknwon args value
calc(10,20,30,40, 60, 80, 90)

# ------------- Dealing with keyword arguments - kwargs---------------#

def unknown_args(**unknown):
    print(unknown)
    
unknown_args(Name="Gary", Surname="Hutson", Age=39)

# ------------- Passing Lists as arguments----------------------------#

def list_power(list_obj, power=2):
    result_list = []
    for val in list_obj:
        result_list.append(val ** power)
    return(result_list)
        
   
list_of_numbs = [2,3,4,5,6,7]
list_power(list_of_numbs, 10)




# ------------- Recursion - function calling itself--------------------#

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)
