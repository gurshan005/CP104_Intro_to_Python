"""
-------------------------------------------------------
[lab 7, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
from functions import sum_squares


target = int(input("Enter a target value (int >= 0): "))

final = sum_squares(target)
   
print(f"The sum of squares closest to and greater than or equal to {target} is: {final}")
