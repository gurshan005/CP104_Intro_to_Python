"""
-------------------------------------------------------
[assignment 6, task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
from functions import detect_prime
number = int(input("input a interger")) 

prime = detect_prime(number)

if prime:
    print(f"{number} is true.")
else:
    print(f"{number} is false.")
    
    