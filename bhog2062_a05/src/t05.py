"""
-------------------------------------------------------
[assignment 5, task 5]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""

from functions import range_addition 

start = int(input("input start number"))

increment = int(input("input range increment "))

count = int(input("input the number of values in the range"))

total = range_addition(start, increment, count)

print(total)
