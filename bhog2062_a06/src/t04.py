"""
-------------------------------------------------------
[assignment 6, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
""" 
from functions import count_of_digits 

number = int(input("input a number"))

digits = count_of_digits(number)

print(f"the number of digits in {number} is : {digits}")