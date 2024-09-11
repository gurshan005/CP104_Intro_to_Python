"""
-------------------------------------------------------
[lab 8, task 10]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""
from functions import min_search

input_values = input("Enter a list of values separated by spaces: ")
values = [int(val) for val in input_values.split()]

indexes = min_search(values)

print(f" min value found at index : {indexes}")