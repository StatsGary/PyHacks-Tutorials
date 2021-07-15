# =============================================================================
# Title             PyHacks - Matplotlib - Intro
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      15/07/2021
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

#Create a fake dataset to plot 
x_axis = np.array([0,1,2,3,4,5,6,7,8])
y_axis = np.array([100, 123, 145, 102, 99, 66, 55, 43, 56])

plt.plot(x_axis, y_axis)
plt.show()

# -----------------------Adding markers to the plot----------------------------
# Marker	Description
# =============================================================================
# 'o'	Circle
# '*'	Star
# '.'	Point
# ','	Pixel
# 'x'	X
# 'X'	X (filled)
# '+'	Plus
# 'P'	Plus (filled)
# 's'	Square
# 'D'	Diamond
# 'd'	Diamond (thin)
# 'p'	Pentagon
# 'H'	Hexagon
# 'h'	Hexagon
# 'v'	Triangle Down
# '^'	Triangle Up
# '<'	Triangle Left
# '>'	Triangle Right
# '1'	Tri Down
# '2'	Tri Up
# '3'	Tri Left
# '4'	Tri Right
# '|'	Vline
# '_'	Hline
# =============================================================================
plt.plot(y_axis, marker='o')
plt.show()

# Make the point a star
plt.plot(y_axis, marker="*")
plt.show()


# -----------------------Marker formatting ------------------------------------
# Colouration
# =============================================================================
# Color Syntax	Description
# 'r'	            Red	
# 'g'	            Green	
# 'b'	            Blue	
# 'c'	            Cyan	
# 'm'	            Magenta	
# 'y'	            Yellow	
# 'k'	            Black	
# 'w'	            White
# =============================================================================

# Marker sizing
plt.plot(y_axis, marker='o', ms=20)
plt.show()

# Colour marker edge
plt.plot(y_axis, marker="o", ms=20, mec='r')
plt.show()

# Colour marker fill
plt.plot(y_axis, marker='*', ms=20, mfc='r', mec='k')
plt.show()

# Make edge and face same colour
plt.plot(y_axis, marker='o', ms=10, mfc='k', mec='k')

# Use hexadecimal custom colours
plt.plot(y_axis, marker='o', ms=10, mfc='#6bb3ea', 
         mec='#6bb3ea')
plt.show()

