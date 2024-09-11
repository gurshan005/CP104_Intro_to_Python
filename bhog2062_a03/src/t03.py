"""
-------------------------------------------------------
[assignment 3, task 3]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-21-10"
-------------------------------------------------------
"""

from functions import extract_date 

date_number = int(input("input a int in the format YYYYMMDD")) 

year, month , day = extract_date(date_number)

print(f"{year}, {month}, {day}")