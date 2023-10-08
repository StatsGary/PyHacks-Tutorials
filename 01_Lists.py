# =============================================================================
# Title             PyHacks - Lists, Looping and List Comprehensions
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      01/07/2021
# =============================================================================

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.

"""

# =============================================================================
# #-----------------------------List Method Lookup -------------------------#
# =============================================================================
# Method	    Description
# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list
# =============================================================================
# ------------- Creating your first list------------------#
# A list is a built in data type, among 3 additional types, that 
# allow you to store multiple items in a single variable

import numpy as np

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
yearly_coding_errors_reality = []
for i in yearly_coding_errors:
    reality = int(i * 1.25)
    yearly_coding_errors_reality.append(reality)
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

# ------------- Sortng lists ----------------------------#
print("[MSG] Sorting the list ascending")
yearly_coding_errors.sort()
print(yearly_coding_errors)

print("[MSG] Sorting the list descending")
yearly_coding_errors.sort(reverse=True)
print(yearly_coding_errors)

# ------------- Copying lists ----------------------------#
covered_so_far = ["List fundamentals", "Accessing List Items",
                  "Adding List Items", "Changing List Items",
                  "Add List Items", "Remove List Items",
                  "Loop Items", "List Comprehension", "Sorting lists"]

print(covered_so_far)

# Copy our newly created list
first_method = covered_so_far.copy()
second_method = list(covered_so_far)
print(first_method, second_method)

# ------------- Joining Two Lists ----------------------------#
list_length = len(covered_so_far)
# Add list item to keep track
covered_so_far.insert(list_length+1, "Copying lists")
print(covered_so_far)


# Join the first and second method lists together
joined_list_one = first_method + prog_languages
print(joined_list_one)

# Using the append method
years_experience = [1,2,3,4]
salary = [45000, 50000, 53000, 62000]

for i in years_experience:
    salary.append(i)
    
print(salary)


