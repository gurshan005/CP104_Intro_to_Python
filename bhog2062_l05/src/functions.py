#CONSTANTS 




FIVE = 1.05
ONEPOINTFIVE = 1.015 
TWO= 1.02 
THREE=1.03
ONE=1.01

def magic_date (day, month, year):

    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """ 
    
    if day > 0 and month > 0 and year > 0:
        
        magic = day * month == year
        return magic
    else:
        # If any of the parameters is not greater than 0, it's not a valid date.
        return False 





def closest(target, v1 , v2 ):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
"""
   
    
    
    diff1 = abs(target - v1)
    diff2 = abs(target - v2)
    
    if diff1 == diff2:
        result = v1
    else:
        if diff1 < diff2:
            result = v1
        else:
            result = v2

    return result

def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    
    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else :
    
        pass
    
    return numeral

def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    if status == 'F':
        if years >= 10:
            new_salary = salary * 1.05  # 5% raise for full-time employees with 10 or more years
        elif years < 4:
            new_salary = salary * 1.015  # 1.5% raise for full-time employees with less than 4 years
        else:
            new_salary = salary * 1.02  # 2% raise for other full-time employees
    elif status == 'P':
        if years >= 10:
            new_salary = salary * 1.03  # 3% raise for part-time employees with 10 or more years
        elif years < 4:
            new_salary = salary * 1.01  # 1% raise for part-time employees with less than 4 years
        else:
            new_salary = salary * 1.02  # 2% raise for other part-time employees
    else:
        raise ValueError("Invalid employment status. Use 'F' for Full Time or 'P' for Part Time.")

    return new_salary


def ticket(age,is_student):
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """ 
    
    if age < 3:
        price = 0.00
    elif age >= 65:
        price = 4.00
    elif 10 <= age < 18:
        if is_student:
            price = 1.00  # Student of this school
        else:
            price = 3.00
    elif 18 <= age < 65:
        price = 5.00
    elif 3 <= age < 10:
        price = 2.00
    else:
        price = None

    return price

