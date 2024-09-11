"""
-------------------------------------------------------
[assignment 5 functions]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
#task 1
def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    
    if number < 0:
        product= None  # Factorial is not defined for negative numbers
    elif number == 0:
        product= 1
    else:
        product = 1
        for i in range(1, number + 1):
            product *= i
        return product

#task 2
def calories_treadmill(per_min, minutes):
    
    """
    -------------------------------------------------------
    Running on a treadmill burns a certain number of calories. 
    calories_treadmill prints a table of the number of 
    calories burned every five minutes given the number of 
    calories burned per minute (per_min) an the total number
    of minutes run (minutes)
    ------------------------------------------------------
    """

    total_calories_burned = 0
    
    minutes = int(minutes)
# Iterate through each five-minute interval and print the calories burned
    for minute in range(5, minutes + 1, 5):
        calories_burned = per_min * 5
        total_calories_burned += calories_burned
        
        print(f"Minutes: {minute},Total Calories: {total_calories_burned}")
        
    
        
    #task 3    
def arrow_up(rows):   
    """
    -------------------------------------------------------
    makes an arrow given an int
    ------------------------------------------------------
    """

    for i in range(rows):
        spaces = ' ' * (rows - i - 1)
        if i == 0:
            print(f'{spaces}#')
        else:
            print(f'{spaces}#{" " * (i - 1)}#')

            return None 
#task 4
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("   ", end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:4}", end="")
    print("\n" + " " * 4 + "-" * 25)

    # Print the multiplication table
    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            result = i * j
            print(f"{result:4}", end="")
        print()
    return None 
    #task 5    
def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    current_value = start

    for _ in range(count):
        total += current_value
        current_value += increment

    return total
