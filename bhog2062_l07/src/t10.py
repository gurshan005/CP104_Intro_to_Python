"""
-------------------------------------------------------
[lab 7, task 10]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""

from functions import employee_payroll

total, average = employee_payroll()

print(f"Total net employee wages: ${total:.2f}")
print(f"Average employee net wages: ${average:.2f}")
