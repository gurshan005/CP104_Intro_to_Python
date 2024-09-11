"""
-------------------------------------------------------
[lab 7, task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
from functions import power_of_two 

power_value = int(input("Enter a power value: "))
power = power_of_two(power_value)
print(f"The nearest power of 2 greater than or equal to {power_value} is {power}")
