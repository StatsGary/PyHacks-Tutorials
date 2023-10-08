# =============================================================================
# Title             PyHacks - Matplotlib - Line Charts
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      15/07/2021
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

y = np.array([10,40, 34, 54, 65, 32, 89, 25, 45, 56])

# ---------------------LINE STYLES--------------------------------------------

# Line styles
plt.plot(y, linestyle='dotted')
plt.show()

# Dashed line
plt.plot(y, linestyle ='dashed')
plt.show()

# Shorter 
plt.plot(y, ls= ':')
plt.show()

#---------------------LINE COLOURING------------------------------------------
# By colour
plt.plot(y, color='r')
plt.show()

# With Hex
plt.plot(y, color='#207c5b')
plt.show()

#---------------------LINE WIDTH----------------------------------------------
plt.plot(y, linewidth='17')
plt.show()

#---------------------MULTIPLE LINES-------------------------------------------

l1 = np.array([10,20, 21, 11, 12, 13])   
l2 = l1 * 2
plt.plot(l1)
plt.plot(l2)
plt.show()



