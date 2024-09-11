"""
-------------------------------------------------------
[lab 5, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-20-10"
-------------------------------------------------------
"""

from functions import closest 


target = float(input("the target value"))

v1 = float(input("the first comparison value"))

v2 = float(input("the second comparison value")) 

result = closest(target, v1, v2)

print(result)