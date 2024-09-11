'''
Created on Nov. 18, 2023

@author: gurshanbhogal
'''
from functions import verify_sorted 


user_input = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(value) for value in user_input]

in_order, index = verify_sorted(numbers)

if in_order:
    print(f"{in_order}, {index}")
else:
    print(f"{in_order}, {index}")