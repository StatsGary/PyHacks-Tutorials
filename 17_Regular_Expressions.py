# =============================================================================
# Title             PyHacks - Classes  - Regular Expressions aka regex
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      13/07/2021
# =============================================================================

import re

txt = "Nottingham is great"
srch = re.search("^Nottingham.*great$", txt)
print(srch)

# Regex functions

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