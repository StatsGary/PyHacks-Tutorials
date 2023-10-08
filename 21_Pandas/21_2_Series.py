# =============================================================================
# Title             PyHacks - Pandas - Starting off
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      14/07/2021
# =============================================================================

import pandas as pd

#--------------------------SERIES --------------------------------------

# A Pandas series is a column in a table. It is a 1D array of data of any type

simp_series = [1,3,4,5,6]
s1 = pd.Series(simp_series)
print(s1)

# ------------------------- LABEL INDEX ---------------------------------
# If nothing is specified for the label, the index number gets used
print(s1[0])
# Create your own labels on a series with the index argument
s2_lbl = pd.Series(simp_series, 
                   index=["ob1", "ob2", "ob3", "ob4", "ob5"])

print(s2_lbl)
# Index the labels
print(s2_lbl["ob2"])

# ------------------------- KEY/VALUE Series ---------------------------------

ed_admissions = {"Monday": 434, "Tuesday": 324, "Wednesday": 236,
                 "Thursday": 234, "Friday": 345}

ed_s = pd.Series(ed_admissions)
print(ed_s)

# The keys of the dictionary then become the labels of the series
# To use specific keys

ed_spec_s = pd.Series(ed_admissions, index=["Thursday", "Friday"])
print(ed_spec_s)