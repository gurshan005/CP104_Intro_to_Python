"""
-------------------------------------------------------
[lab 7, functions]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
from random import randint

def hi_lo_game(high):
    """
     -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0

    while True:
        guess = int(input("Guess: "))
        count += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")
            break

    print(f"You made {count} guesses.")
    return count


def power_of_two(target):
    """
       -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    while power < target:
        power *= 2
    return power


def sum_squares(target):
    """
   -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    sum_of_squares = 0
    i = 1

    while sum_of_squares < target:
        sum_of_squares += i * i
        i += 1

    # If target is 0, set the result to 1
    if target == 0:
        final = 1
    else:
        final = sum_of_squares

    return final


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    #constants
    total_wages = 0
    employee_count = 0
    TAX_RATE = 0.03625
    OVERTIMERATE = 1.5
    OVERTIME =40
    while True:
        employee_id = int(input("Employee ID: "))
        
        if employee_id == 0:
            break
        
        hourly_wage = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))

        if hours_worked > OVERTIME:
            regular_pay = OVERTIME * hourly_wage
            overtime_pay = (hours_worked - OVERTIME) * (OVERTIMERATE * hourly_wage)
            gross_salary = regular_pay + overtime_pay
        else:
            gross_salary = hours_worked * hourly_wage

        net_salary = gross_salary - (gross_salary * TAX_RATE)

        print(f"Net payment for employee {employee_id}: ${net_salary:.2f}\n")

        total_wages += net_salary
        employee_count += 1

    if employee_count == 0:
        total_wages= 0  # No employees, so total and average are both 0
        average_wages =0
    else:
        average_wages = total_wages / employee_count
        return total_wages, average_wages
    
    
    
def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0

    while True:
        # Ask the user for the cost of breakfast, lunch, and supper for one day
        b_cost = float(input("Enter the cost of breakfast for the day: $"))
        l_cost = float(input("Enter the cost of lunch for the day: $"))
        s_cost = float(input("Enter the cost of supper for the day: $"))

        # Add the daily costs to the running totals
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        a_total += (b_cost + l_cost + s_cost)

        another_day = input("Do you want to enter data for another day? (yes/no): ").lower()

        if another_day != 'yes':
            break

    return b_total, l_total, s_total, a_total
    
    
