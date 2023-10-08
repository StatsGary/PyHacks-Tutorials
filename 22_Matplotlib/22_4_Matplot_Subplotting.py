# =============================================================================
# Title             PyHacks - Matplotlib - Subplotting
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      15/07/2021
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

#----------------------Sub plotting--------------------------------------------
# First plot
x = np.array([1,4,5,6,7])
y = np.array([3,8,1,10,5])

plt.subplot(1,2,1)
plt.plot(x,y)

# Second plot

x = np.array([1,4,5,6,7])
y = y *2
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

#----------------------The subplots() Function---------------------------------
# The subplots() function takes three arguments that describes the layout of the figure.
# The layout is organized in rows and columns, which are represented by the first and second argument.
# The third argument represents the index of the current plot.


# ---------------------DRAW TWO PLOTS ON TOP-----------------------------------
# First plot
x = np.array([1,4,5,6,7])
y = np.array([3,8,1,10,5])

plt.subplot(2,1,1)
plt.plot(x,y)

# Second plot

x = np.array([1,4,5,6,7])
y = y *2
plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.show()


# -------------------DRAW SIX PLOTS--------------------------------------------
#1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x,y)
#2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x,y)
#3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x,y)
#4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x,y)
#5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x,y)
#6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.show()