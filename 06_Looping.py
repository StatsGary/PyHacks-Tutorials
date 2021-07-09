# =============================================================================
# Title             PyHacks - Looping For and While Iteration
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      07/07/2021
# =============================================================================


# ------------- While Loops (do while TRUE until FALSE)------------------#

i = 1
terminate = 100
while i <= terminate:
    print("The val of i is:{}".format(i))
    i += 1
    # i = i+1
else:
    print("The value of i is no longer less than 100, therefore the evaluation is FALSE.")
    
# The Break statement
i = 1
while i < terminate:
    print(i)
    if i == 50:
        break
    i += 1
    
# The continue statement

i = 1
while i < terminate:
    i += 1
    if i % 2:
        print("Found the odd value: {}".format(i))
        continue
    print("This must be even then: {}".format(i))
    

# ------------- For Loops (For Each Item in object)------------------#    
    
# Looping through characters in a string
for char in "I love Python, as it is so awesome!":
    print("The letter is {}".format(char))
    
# Break statement
programming_langs = ["Python", "R", "SQL"]
for i in programming_langs:
    print(i)
    if i == "R":
        break

# Continue statement
programming_langs = ["Python", "R", "SQL"]
found_val = []
for i in programming_langs:
    print(i)
    if i == "R":
        found_val.append(i)
        print("I know you like R as well, but keeping printing..")
        continue
    
# Looping through a range object
for i in range(10): 
    print(i+1)
    
# Range with start and end parameters
for i in range(1,10):
    print(i)
    
# Increment by a value
for i in range(0, 100, 10):
    print(i)
    
# Nested Loops
descriptive = ["Awesome", "Excellent", "Fab"]

for x in descriptive:
    for y in programming_langs:
        print(x, y)
        
# Time table example
for x in range(1,11):
    for y in range(1,11):
        result = x * y
        print(result)

# You can add a pass statement the same as with the 



