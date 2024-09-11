"""
-------------------------------------------------------
[lab 4, task 7]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-6-10"
-------------------------------------------------------
"""
from functions import total_change
nickels = int(input()) 

dime = int(input()) 

quarters = int(input())  

loonie = int(input())  

toonie = int(input())  

total = total_change(nickels,dime,quarters,loonie,toonie) 

print (float(total)) 

