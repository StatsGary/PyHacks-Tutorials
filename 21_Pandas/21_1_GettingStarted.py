# =============================================================================
# Title             PyHacks - Pandas - Starting off
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      14/07/2021
# =============================================================================

import pandas as pd

df = {
      'rock_bands': ['Nirvana', 'Foo Fighters', 'Metallica'],
      'albums_sold': [650000, 780000, 540000]
      }


df = pd.DataFrame(df)
print(df)

# Get the pandas version 
print(pd.__version__)