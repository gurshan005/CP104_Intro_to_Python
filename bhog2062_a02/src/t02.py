"""
-------------------------------------------------------
[assignment2 task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
""" 


value = int(input("enter a positive two digit interger ")) 

tens = value //10 

ones = value % 10 

difference = tens - ones 

print(f"the difference of the digits of {value} is {difference} ")

