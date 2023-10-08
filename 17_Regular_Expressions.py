# =============================================================================
# Title             PyHacks - Classes  - Regular Expressions aka regex
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================

# Character codes for regex
# =============================================================================
# Character	   Description	                                 Example
# []	       A set of characters	                         "[a-m]"
# \	           Signals a special sequence	                 "\d"
# .	           Any character (except newline character)	     "he..o"
# ^	           Starts with	                                 "^hello"
# $	           Ends with	                                 "world$"
# *	           Zero or more occurrences	                     "aix*"
# +	           One or more occurrences	                     "aix+"
# {}	       Exactly the specified number of occurrences	 "al{2}"
# |	           Either or	                                 "falls|stays"
# ()	       Capture and group	
# =============================================================================

# Special Sequences
# =============================================================================
# Character	Description	Example
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
# \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
# 	(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"ain\b"
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
# 	(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"ain\B"
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
# \D	Returns a match where the string DOES NOT contain digits	"\D"
# \s	Returns a match where the string contains a white space character	"\s"
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
# 
# =============================================================================

# Sets
# =============================================================================
# Set	        Description
# [arn]	    Returns a match where one of the specified characters (a, r, or n) are present
# [a-n]	    Returns a match for any lower case character, alphabetically between a and n
# [^arn]	    Returns a match for any character EXCEPT a, r, and n
# [0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9]	    Returns a match for any digit between 0 and 9
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
# 
# 
# =============================================================================
import re
txt = "Nottingham is great"
srch = re.search("^Nottingham.*great$", txt)
print(srch)

# ------------------------------Regex functions-------------------------------
# Findall
findit = re.findall("Nottingham", txt)
print(findit)
# Search to find whitespace
ws = re.search("\s", txt)
print(ws.start())
# Splitting text with the split function
splitted = re.split("\s", txt)
print(splitted)
max_split = re.split("\s", txt,1)
print(max_split)
# Replacing text with sub
replaced = re.sub("\s", "*", txt)
print(replaced)
name_replaced = re.sub("Nottingham", "Reykjavik", txt)
print(name_replaced)

# ------------------------------Match Objects-------------------------------
# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

ot = re.search("ot", txt)
print(ot)
# Print the position start and end of the first match occurence
idx_rng= re.search(r"\bN\w+", txt)
print(idx_rng.span())
print(idx_rng.string) #Print the string passed to the function
print(idx_rng.group())