"""
-------------------------------------------------------
[assignment 7, task 3]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
from functions import get_indexes

user_input = input("Enter a list of values separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

target_number = int(input("Enter the target number to look for: "))

index_list = get_indexes(numbers, target_number)
print(f"{index_list}")