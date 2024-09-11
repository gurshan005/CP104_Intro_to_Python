"""
-------------------------------------------------------
[lab 8, functions]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""
def list_factors(number):
    """
    -------------------------------------------------------
    list_factors takes an integer greater than 0 as a parameter 
    (number) and returns a list of the factors that make up that 
    number excepting the number itself. An integer's factors are 
    the whole numbers that the integer can be evenly divided by.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Returns:
        factors - A list of factors
    ------------------------------------------------------
    """
    # Initialize an empty list to store factors
    factors = []

    # Iterate from 1 to number to find factors
    for i in range(1, number):
        # Check if the number is divisible by i (i is a factor)
        if number % i == 0:
            factors.append(i)

    return factors 

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []

    while True:
        try:
            user_input = int(input("Enter a positive number (enter 0 to stop): "))
            if user_input == 0:
                break  # Stop if the user enters 0
            elif user_input > 0:
                number_list.append(user_input)  # Add positive numbers to the list
            else:
                print("Negative numbers are ignored. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return number_list



def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """


    index_list = []

    # Iterate through the indices of numbers
    for i in range(len(numbers)):
        # Check if the element at the current index is equal to target_number
        if numbers[i] == target_number:
            index_list.append(i)

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    minuend[:] = [value for value in minuend if value not in subtrahend]

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """ 
    n = len(numbers)

    for i in range(1, n):
        # Check if the current element is less than the previous one
        if numbers[i] < numbers[i - 1]:
            return False, i

    # If the loop completes, the list is sorted
    return True, -1

    