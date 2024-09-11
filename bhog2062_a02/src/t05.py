"""
-------------------------------------------------------
[assignment 2 task 5]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
""" 
 

length = float(input("foundation length "))

width = float (input("width ")) 

height = float (input ("height "))

wall_height = float (input("input the wall height "))

costofconcrete = float(input("enter the cost of concrete ($/m^3"))

costofbricks = float(input("enter the cost of bricks"))

concretecost = costofconcrete*(length*width*height)

bricksneeded= (2*(wall_height*width)) + (2*(wall_height*length))

brickcost =  bricksneeded *costofbricks

print("concrete needed for foundation (m^3): ", length*width*height) 

print("cost of concrete: ", concretecost)

print("bricks needed for walls (m^2)", (2*(wall_height*width)) + (2*(wall_height*length)))

print(f"cost of bricks: {brickcost:,.2f}") 

print(f"total cost: {brickcost+concretecost:,.2f}") 



 

