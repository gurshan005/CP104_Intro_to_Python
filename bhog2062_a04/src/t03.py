"""
-------------------------------------------------------
[assignment 4, task 3]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""

from functions import largest_average 

val1 = float(input("Enter the first value: "))
val2 = float(input("Enter the second value: "))
val3 = float(input("Enter the third value: "))

average =largest_average(val1, val2, val3)

print(f"largest_average({val1}, {val2}, {val3}) -> {average}")
