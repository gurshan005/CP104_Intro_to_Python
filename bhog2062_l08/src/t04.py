"""
-------------------------------------------------------
[lab 8, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""

from functions import generate_integer_list

n = int(input("the number of values to generate"))

low = int(input("low value range"))

high = int(input("high value range"))

values = generate_integer_list(n, low, high)

print(values)