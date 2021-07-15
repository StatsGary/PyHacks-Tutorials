# =============================================================================
# Title             PyHacks - Matplotlib - Labelling
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      15/07/2021
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

crime_rate = np.array([45.5,52.3,56.6,60.3,64.2,67.6,70.3])
offenders_imprisioned = np.array([24, 34, 37, 39, 45, 48, 56])

y = crime_rate
x = offenders_imprisioned

#----------------------LABELLING----------------------------------------------

# Create the plot and label x and y
plt.plot(x, y)
plt.xlabel("Offenders Imprisioned")
plt.ylabel("Crime Rate")
plt.show()

# Add a title to the plot
plt.plot(x, y)
plt.title("Crime vs imprisioned offenders")
plt.xlabel("Offenders Imprisioned")
plt.ylabel("Crime Rate")
plt.show()

# Set font for title and labels
font1 = {'family':'serif','color':'black','size':20}
font2 = {'family':'serif','color':'navy','size':15}

plt.title("Crime vs imprisioned offenders", fontdict = font1)
plt.xlabel("Offenders Imprisioned",fontdict = font2 )
plt.ylabel("Crime Rate", fontdict = font2)
plt.plot(x, y)
plt.show()

# Position the title

plt.title("Crime vs imprisioned offenders", loc="right")
plt.xlabel("Offenders Imprisioned")
plt.ylabel("Crime Rate")
plt.plot(x, y)
plt.show()


#----------------------GRIDS--------------------------------------------------
plt.title("Crime vs imprisioned offenders", loc="center")
plt.xlabel("Offenders Imprisioned")
plt.ylabel("Crime Rate")
plt.plot(x, y)
plt.grid()
plt.show()

# Specify which grid lines to show
plt.title("Crime vs imprisioned offenders", loc="center")
plt.xlabel("Offenders Imprisioned")
plt.ylabel("Crime Rate")
plt.plot(x, y)
plt.grid(axis = 'x') #Show x grids
plt.grid(axis = 'y') #Show y grids
plt.show()

#Format grid lines
