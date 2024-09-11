"""
-------------------------------------------------------
[lab 5, task 8]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-20-10"
-------------------------------------------------------
"""
from functions import roman_numeral
n = int(input("roman numeral "))

numeral = roman_numeral(n)

if numeral is not None:
    print(f"The Roman numeral for {n} is {numeral}")
else:
    print(f"Sorry, {n} is not between 1 and 10, so there is no Roman numeral conversion.")
    
    
    