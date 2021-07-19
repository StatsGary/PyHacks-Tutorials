# =============================================================================
# Title             PyHacks - Matplotlib - Scatter Charts
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      15/07/2021
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
#Random x and y numpy arrays 
x = np.array([5,7,8,7,5,19,4,10,5,14,11,8])
y = np.array([101,90, 89,88, 121, 98, 106, 96, 89, 56, 11, 89])
plt.scatter(x,y)
# Add additional scatter chart to the mix
x = np.array([x *3])
y = np.array([y * 2.5])
plt.scatter(x, y)
plt.show()


#--------------------Setting scatter chart colours------------------------
x = np.array([5,7,8,7,5,19,4,10,5,14,11,8])
y = np.array([101,90, 89,88, 121, 98, 106, 96, 89, 56, 11, 89])
plt.scatter(x,y, color="blue")
# Add additional scatter chart to the mix
x = np.array([x *3])
y = np.array([y * 2.5])
plt.scatter(x, y, color = "#ff0000")
plt.show()

#------------------------ Colour each dot ---------------------------------
x = np.array([5,7,8,7,5,19,4,10,5,14,11,8])
y = np.array([101,90, 89,88, 121, 98, 106, 96, 89, 56, 11, 89])
dot_colours = np.array(["red", "blue", "green", "pink", 
                        "orange", "#4d6189", "navy", "hotpink",
                        "#efef26", "grey", "black", "purple"])

plt.scatter(x, y, color=dot_colours)
plt.show()

#--------------------Using a colour map gradient----------------------------