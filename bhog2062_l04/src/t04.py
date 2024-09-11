"""
-------------------------------------------------------
[lab 4, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-6-10"
-------------------------------------------------------
"""
from functions import square_pyramid

base = float(input())
height = float(input())

sh, area, vol = square_pyramid(base, height)

print(f"{sh},{area},{vol}")

