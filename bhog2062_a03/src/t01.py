"""
-------------------------------------------------------
[assignment 3, task 1]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-21-10"
-------------------------------------------------------
"""
from functions import footage_to_acres 

square_feet = float(input("enter your square footage"))

acres = footage_to_acres(square_feet)

print(acres)