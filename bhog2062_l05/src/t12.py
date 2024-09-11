"""
-------------------------------------------------------
[lab 5, task 12]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-20-10"
-------------------------------------------------------
"""
from  functions import pay_raise

status = input("type your status")

years = int(input("years of service"))

salary = float(input("input salary"))

new_salary = pay_raise(status, years, salary)

print(f"The new salary is: ${new_salary:.2f}")
