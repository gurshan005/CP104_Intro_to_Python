"""
-------------------------------------------------------
[assignment 6, task 3]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
from functions import interest_table 

principal_amount = float(input("original value of the loan "))

interest_rate = float(input("yearly interest rate"))

payment = float(input("the monthly payment"))

interest_table(principal_amount, interest_rate, payment)