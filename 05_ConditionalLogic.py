# =============================================================================
# Title             PyHacks - Conditional Logic - If Else Elseif 
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      07/07/2021
# =============================================================================
# =============================================================================
# Logical Operators
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# =============================================================================

# ------------- Simple If Statement  ------------------#

code_exp = 6
role_code_exp = 4

if code_exp > role_code_exp:
    print("Great you have got the job!")
    
# Watch this code error out without indentation
# if code_exp > role_code_exp:
# print("Great you have got the job!")

# ------------- Throw in the Elif statement-------------#

if role_code_exp > code_exp:
    code_deficit = abs(role_code_exp-code_exp)
    print("Sorry, you need {} years experience to get a coding role here!".format(code_deficit))
elif role_code_exp <= code_exp:
    print("Wow! You know how to code in Python!")
    
# ------------- Throw in the Else statement-------------#
if role_code_exp > code_exp:
    code_deficit = abs(role_code_exp-code_exp)
    print("Sorry, you need {} years experience to get a coding role here!".format(code_deficit))
elif role_code_exp <= code_exp:
    print("Wow! You know how to code in Python!")
else:
    print("Unsure how to assess this?")
    
# ------------- Short hand if else ---------------------------#

print("Your coding experience rocks!") if code_exp > role_code_exp else print("Good, but need more time to develop")

# ------------- AND Keyword ---------------------------#

    
# Using the AND keyword
code_exp = 6
role_code_exp = 4
job_exp = 10
role_job_exp = 3
your_comb_exp = int(code_exp + job_exp)


if code_exp > role_code_exp and job_exp > role_code_exp:
    print("You have the coding and job experience needed.")
    

# ------------- OR Keyword ---------------------------#

if code_exp > role_code_exp or job_exp > role_job_exp:
    print("We are looking for a balance between coding and job experience. The job is yours!")
    
# ------------- Nested if ---------------------------#

code_exp = 6 

if code_exp > 2:
    print("Candidate for junior developer")
    if code_exp > 5:
        print("Developer")
        if code_exp > 7:
            print("Senior Developer")
else:
   print("Not captured")


# ------------- The Pass statement --------------------#

if code_exp > 1:
    pass
    #Working on this