"""
-------------------------------------------------------
[assignment 7, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""

from functions import list_subtract

minuend_list = input("Enter a list of values for minuend separated by spaces: ").split()
minuend_list = [int(value) for value in minuend_list]

subtrahend_list = input("Enter a list of values for subtrahend separated by spaces: ").split()
subtrahend_list = [int(value) for value in subtrahend_list]

list_subtract(minuend_list, subtrahend_list)

print(f"The updated minuend list after subtraction is: {minuend_list}")