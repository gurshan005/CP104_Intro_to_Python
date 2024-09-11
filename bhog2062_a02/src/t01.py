"""
-------------------------------------------------------
[assignment 2 task 1]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-6-10"
-------------------------------------------------------
"""

#Constants 

TAXRATE = 0.185

sales = float (input("enter the projected total sales"))


print("projected tax reoprt ")
print("--------------------------- ")
print(f"total sales:      {sales}")
print(f"annual tax rate   {TAXRATE*100} ")
print("---------------------------")
print ("tax: " , sales*TAXRATE) 