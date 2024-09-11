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
def total_wins():
    purple_count = 0
    gold_count = 0

    while True:
        result = input("Enter game result or press Enter to finish: ").lower()

        if result == "":
            break

        if result == "purple":
            purple_count += 1
        if result == "gold":
            gold_count += 1
            
    return purple_count, gold_count 
        
        
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if number <= 1:
        prime = False

    divisor = 2
    
    while divisor * divisor <= number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    else: 
        prime = True
    
    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    # Convert interest_rate to a decimal
    monthly_interest_rate = interest_rate / 100 / 12
    
    # Initialize variables
    remaining_balance = principal_amount
    month = 1

    # Print loan details
    print("Principal:   ${:.2f}".format(principal_amount))
    print("Interest rate: {:.2f}%".format(interest_rate))
    print("Monthly payment: ${:.2f}".format(payment))
    print("----------------------------------")
    print("{:<5} {:<10} {:<10} {:<10}".format("Month", "Interest", "Payment", "Balance"))
    print("----------------------------------")

    while remaining_balance > 0:
        # Calculate monthly interest
        monthly_interest = remaining_balance * monthly_interest_rate
        
        # Ensure the payment is not more than the remaining balance
        actual_payment = min(payment, remaining_balance + monthly_interest)
        
        # Calculate the remaining balance
        remaining_balance = remaining_balance + monthly_interest - actual_payment

        # Print the row in the table
        print("{:<5} {:<10.2f} {:<10.2f} {:<10.2f}".format(month, monthly_interest, actual_payment, remaining_balance))

        # Increment month counter
        month += 1
        
        
        
        
        
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    number = abs(number)
    
    digits = 1 if number == 0 else 0


  
    while number > 0:
        number //= 10
        digits += 1

    return digits

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    
    total = 0
    factor = 1

    while factor <= number // 2:
        if number % factor == 0:
            total += factor

        factor += 1

    return total if number >= 1 else 0
