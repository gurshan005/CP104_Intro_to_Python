"""
-------------------------------------------------------
[lab 3, task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-29-11"
-------------------------------------------------------
"""

number= float(input("input a float")) 

percent = float(input("input a percent as a float:")) 

decimal = percent/100

calculation = (decimal*number) 


print(f" {percent} discount on {number} is" + " {:.1f}".format(calculation))
