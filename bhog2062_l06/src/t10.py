"""
-------------------------------------------------------
[lab 6, task 10]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-27-10"
-------------------------------------------------------
""" 
from functions import treadmill 

burnt_per_minute = float(input("burned calories")) 

start = int(input("start time in minutes"))

end = int(input("end time in minutes"))

inc = int(input("increment in minutes"))

treadmill(burnt_per_minute, start, end, inc) 
