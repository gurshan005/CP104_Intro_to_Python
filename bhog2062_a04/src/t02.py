"""
-------------------------------------------------------
[assignment, task 2]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""
from functions import pollution_ranking 

air_quality_index = int(input("air quality number"))

pollution = pollution_ranking(air_quality_index) 

print(pollution)