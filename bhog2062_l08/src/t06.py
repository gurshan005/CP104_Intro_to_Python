"""
-------------------------------------------------------
[lab 8, task 6]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""
from functions import list_stats

input_values = input("Enter a list of values separated by spaces: ")

values = [float(val) for val in input_values.split()]

smallest, largest, total, average = list_stats(values)

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Average: {average}")