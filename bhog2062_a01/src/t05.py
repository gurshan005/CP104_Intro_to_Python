"""
-------------------------------------------------------
[assignment 1, task 5]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-30-09"
-------------------------------------------------------
"""


p = float(input("enter your principal amount"))

interest = float(input("enter your intrest rate"))

r = interest/100


years = int(input("the amount of years money has been borrowed"))

n= int(input("number of times the interest is compounded in a year"))

print( p*(1+r/n)**(n*years))
        

