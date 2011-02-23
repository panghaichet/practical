# Filename: samanthasjw_p01q02.py
# Name: Samantha Siau Jing Wen
# Description: Input radius and length of a cylinder and computes its volume

# Prompt user for radius in m
radius = float(input("Enter radius of cylinder in m: "))


# Prompt user for length in m
length = float(input("Enter length of cylinder in m: "))


# Define pi
from math import pi


# Compute area
area = radius*radius*pi



# Compute volume
volume = area*length



# Display result
#print("{0:20s} {1:.20f} {2:3s}".format("Volume of cylinder: ", volume, "m^3"))
print("{0:20s} {1:.2f} {2:3s}".format("Volume of cylinder: ", volume, "m^3"))

#Sam put in the decimals up to 1 place or 2 places. The truncation in the
# format is quite severe as it could be .9 or .1.

# marks = 4/5
