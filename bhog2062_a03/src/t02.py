"""
-------------------------------------------------------
[assignment 3, task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-21-10"
-------------------------------------------------------
"""

from functions import lawn_mow_time 

width = float(input("input the width"))

length = float(input("input the length "))

speed = float (input("input the square metres cut per minute"))

time = lawn_mow_time(width, length, speed)

print(time) 