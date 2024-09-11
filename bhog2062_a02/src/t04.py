"""
-------------------------------------------------------
[assignment 2 task 4]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
""" 


flyers = int(input("enter the amount of flyers"))

people = int(input("enter the number of people"))

total = flyers//people 

remaining = total % people 

print(f"flyers per person : {total}")

print (f"flyers left over {remaining}")


