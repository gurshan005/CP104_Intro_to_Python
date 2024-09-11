"""
-------------------------------------------------------
[lab 8, task 8]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
""" 
from functions import linear_search

input_values = input("Enter a list of values separated by spaces: ")
values = [int(val) for val in input_values.split()]

value = int(input("search value"))

index = linear_search(values, value)

if index != -1:
    print(f"Value {value} found at index {index}")
else:
    print(f"Value {value} not found in the list")






