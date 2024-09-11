"""
-------------------------------------------------------
[assignment 8, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-25-11"
-------------------------------------------------------
"""
from functions import valid_isbn

isbn = str(input("isbn"))

is_valid = valid_isbn(isbn)

print(is_valid)

