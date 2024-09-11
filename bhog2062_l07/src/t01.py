"""
-------------------------------------------------------
[lab 7, task 1]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
from functions import hi_lo_game
high = int(input("Enter the maximum random value: "))
    
count = hi_lo_game(high)

print(f"the user guessed {count} times ")