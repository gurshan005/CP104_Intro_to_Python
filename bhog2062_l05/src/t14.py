"""
-------------------------------------------------------
[lab 5, task 14]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-20-10"
-------------------------------------------------------
"""


from functions import ticket

price = ticket()
if price is not None:
    print(f"The price of the ticket is ${price:.2f}")