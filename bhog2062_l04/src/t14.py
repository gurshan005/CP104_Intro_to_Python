"""
-------------------------------------------------------
[lab 4, task 14]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-6-10"
-------------------------------------------------------
"""

from functions import time_values 

seconds = int(input())

days, hours, minutes = time_values(seconds)

print(minutes, hours, days)