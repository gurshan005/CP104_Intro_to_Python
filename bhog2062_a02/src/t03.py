"""
-------------------------------------------------------
[assignment 2 task 3]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
""" 

value = int (input("enter a YYYYMMDD format"))

year = value//10000 

month = (value//100)%100

day = value %100 

print(f"the formatted date is : {year}/{month:02d}/{day:02d}")