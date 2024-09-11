"""
-------------------------------------------------------
[assignment4, task 5]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""

from functions import hoo_rah

#user for input
user_input = input("Enter an integer: ")

try:

    number = int(user_input)
    result = hoo_rah(number)
    print(f'hoo_rah({number}) -> "{result}"')
except ValueError:
    print("Invalid input. Please enter a valid integer.")