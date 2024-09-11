"""
-------------------------------------------------------
[assignment 3, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-21-10"
-------------------------------------------------------
"""

from functions import multiply_fractions 

num1= int(input("numerator 1"))

den1 = int(input("demonator 1")) 

num2 = int(input("numerator 2"))

den2 = int(input("denomintator 2")) 


num, den, product = multiply_fractions(num1, den1, num2, den2)

print(num,den, product)