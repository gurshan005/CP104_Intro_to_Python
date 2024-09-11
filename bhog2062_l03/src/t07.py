"""
-------------------------------------------------------
[lab 3, task 7]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-29-11"
-------------------------------------------------------
"""
breakfast = float(input("input the cost of breakfast"))

lunch = float(input("input the cost of lunch"))

supper= float(input("input the cost of supper"))

total = breakfast+lunch+supper
print("meal         cost ")
print(f"breakfast ${breakfast:7.2f}")
print(f"lunch     ${lunch:7.2f}")
print(f"breakfast ${supper:7.2f}")

print(f"total     ${total:7.2f}")