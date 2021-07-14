# =============================================================================
# Title             PyHacks - Pandas - DataFrames
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      14/07/2021
# =============================================================================

import pandas as pd

ip_data = {
        "ip_admits": [213,343,124],
        "ed_attends": [456,343,324]
    }

ip_df = pd.DataFrame(ip_data)
print(ip_df)

#------------------- LOCATE ROWS BY LOCATION AND INDEX LOCATION----------------

# Locate rows
print(ip_df.loc[0:1])
# List of indexes
print(ip_df.loc[[0,2]]) #Get the first and last element
# Last entry
print(ip_df.iloc[-1]) #Use iloc to get an integer index
# First entry
print(ip_df.iloc[-len(ip_df)])

#------------------- LOCATE BY INDEXING ---------------------------------------

idx_df = pd.DataFrame(ip_df, index=["Mon", "Tues", "Wed"])
print(idx_df)


