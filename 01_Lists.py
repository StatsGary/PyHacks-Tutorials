# ------------- Creating your first list------------------#
# A list is a built in data type, among 3 additional types, that 
# allow you to store multiple items in a single variable

import numpy as np

#https://www.w3schools.com/python/python_lists_change.asp
#https://www.w3schools.com/python/ref_string_format.asp

prog_languages = ["Python", "R", "C#", "SQL", "Javascript"]
print(prog_languages)
# Get the length of the list
print("The length of the list is: {}".format(len(prog_languages)))

# List can contain mixed data types and are mutable (changeable)
coding_experience = [5, 9, 5, 15, np.nan]
print(coding_experience)

# Return the list's type
list_type = type(prog_languages)
print(list_type)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.

"""

# Creating a list using the relevant list constructor
roles = list(("Senior Data Scientist", "Head of Analytics", 
              "Windows Forms Developer", "Analyst",
              "Web developer"))

print(roles)

# ------------- Access List Items ------------------#
# We will use the example list we created in the previous section
orig_prog = prog_languages.copy()
# Negative indexing
print(prog_languages[-1]) 
# This says get the last item

# Range of indexes
ds_languages = prog_languages[0:2]
print(ds_languages)

# Indexing to a certain position
print(prog_languages[:3])

# Reversing this
print(prog_languages[3:])

# ------------- Change list items ------------------#

# Change list items by index
print("[MSG] Changing list items by index")
prog = prog_languages
prog[0] = "Python Rocks"
print(prog)

# Change index range
print("[MSG] Changing list items by index range")
prog[1:2] = ["R Programming", "C-Sharp"]
print(prog)

# Change multiple items with same value
print("[MSG] Changing multiple items with same value")
prog[2:] = ["Python rocks!!!"]
print(prog)

#Insert items
print("[MSG] Inserting items")
prog_languages.insert(3, "VBA")
print(prog)

# ------------- Append List Items ------------------#

# Append items
code_copy = coding_experience.copy()
# Append item to list
code_copy.append(9)
print(code_copy)

# ------------- Insert List Items ------------------#

#Insert an item in the second list position - remember Python 
#has zero indexing
code_copy.insert(1, 10)
print(code_copy)

# ------------- Extend List -----------------------#
# We will add two lists together now. I will use the code experience and roles
prog_languages.extend(roles)
print(prog_languages)

# ------------- Remove list items by name -----------#
prog = prog_languages.copy()
prog.remove("VBA")
print(prog)

# ------------- Remove list items by index -----------#
prog.pop(1) #If the index is unspecified, pop removes the 
# last item in the list
print(prog)

# Alternate way - also removes the index
del prog[0]
print(prog)

# Delete the list completely
del prog

# Clear the list
ds_languages.clear()
print(ds_languages)

# ------------- Looping lists ------------------------#

for l_item in prog_languages:
    print("The current programming language is: {}".format(l_item))  
# Alternative approach is to use a range() object to get the index number
for l_item in range(len(prog_languages)):
    print(l_item)
    
# ------------- Looping numerical lists----------------#
yearly_coding_errors = [1000, 600, 500, 400]
for i in yearly_coding_errors:
    reality = i * 1.25
    print("User said his yearly coding errors are {}.\nIn reality it is more like {:.0f}".format(i, reality))


# Achieving this with list comprehension 
# List comprehension is a way to embed a iteration statement in a list to return a list
# You will hear it referenced list of lists

# GENERAL SYNTAX
# newlist = [expression for item in iterable if condition == True]

yearly_coding_errors_reality = [int(i * 1.25) for i in yearly_coding_errors]
yearly_coding_errors_limit = [int(i * 1.25) for i in yearly_coding_errors if i > 500]

# Create an iterable
yearly_coding_reviews = [i for i in range(len(yearly_coding_errors))]

# ------------- Looping lists ----------------------------#

