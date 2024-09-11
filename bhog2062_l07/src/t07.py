"""
-------------------------------------------------------
[lab 7, task 7]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
""" 
from functions import meal_costs
print(" Meal Costs ")
b_total, l_total, s_total, a_total = meal_costs()
print("\nMeal Costs Summary:")
print(f"Total breakfasts cost: ${b_total:.1f}")
print(f"Total lunches cost: ${l_total:.1f}")
print(f"Total suppers cost: ${s_total:.1f}")
print(f"Total cost of all meals: ${a_total:.1f}")
