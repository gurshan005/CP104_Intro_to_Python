"""
-------------------------------------------------------
[lab 8, task 1]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""
from functions import get_weekday_name
d = int(input("input the day of the week"))

for d in range (1,8):

    name = get_weekday_name(d)
    
    print(f"{d}: {name} ")