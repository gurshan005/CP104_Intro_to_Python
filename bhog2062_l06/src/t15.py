"""
-------------------------------------------------------
[lab 6, task 15]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-27-10"
-------------------------------------------------------
""" 
from functions import statistics

n = int(input("number"))    

minimum, maximum, total, average = statistics(n)

print(f"({minimum:.2f}, {maximum:.2f}, {total:.2f}, {average:.2f})")

