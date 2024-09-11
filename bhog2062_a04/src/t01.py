"""
-------------------------------------------------------
[assignment, task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""

from functions import day_name



day_num = int(input("Enter a day number (1-7): "))
    
    
if 1 <= day_num <= 7:
    day = day_name(day_num)
    print(f"Day {day_num} is {day}")
else:
    print("Error: Input is not in the valid range (1-7).")
    
    
    
