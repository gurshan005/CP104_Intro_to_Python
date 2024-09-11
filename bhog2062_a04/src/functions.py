"""
-------------------------------------------------------
[assignment 4 functions]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index < 0:
        pollution = "Error"
    elif air_quality_index <= 50:
        pollution = "Good"
    elif air_quality_index <= 100:
        pollution = "Moderate"
    elif air_quality_index <= 150:
        pollution = "Unhealthy for Sensitive Groups"
    elif air_quality_index <= 200:
        pollution = "Unhealthy"
    elif air_quality_index <= 300:
        pollution = "Very Unhealthy"
    else:
        pollution = "Hazardous"
    
    return pollution    


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    
    valid_colors = ["red", "green", "blue"]

    if rgb_colour1 not in valid_colors or rgb_colour2 not in valid_colors:
        rgb_colour = "Error"
    elif rgb_colour1 == rgb_colour2:
        rgb_colour = rgb_colour1
    elif (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red"):
        rgb_colour = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red"):
        rgb_colour = "yellow"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "green"):
        rgb_colour = "aqua"
    else:
        rgb_colour = "Error"

    return rgb_colour 

def hoo_rah(number):
    """
    Determine the response for a given number based on the following rules.

    
    "Hoo" if the number is evenly divisible by 2.
    "Rah" if the number is evenly divisible by 7.
    "Hoo Rah" if the number is evenly divisible by both 2 and 7.
    "Zip" if the number is none of the above.

    Parameters:
    number (int): The integer to be evaluated.

    Returns:
    str: A string representing the result based on the divisibility rules.

    Use:
    result = hoo_rah(14)  # Example usage
    """
    result = "Zip"

    if number % 2 == 0 and number % 7 == 0:
        result = "Hoo Rah"
    elif number % 2 == 0:
        result = "Hoo"
    elif number % 7 == 0:
        result = "Rah"

    return result

def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    largest = None
    second_largest = None

    if val1 >= val2 and val1 >= val3:
        largest = val1
        if val2 >= val3:
            second_largest = val2
        else:
            second_largest = val3
    elif val2 >= val1 and val2 >= val3:
        largest = val2
        if val1 >= val3:
            second_largest = val1
        else:
            second_largest = val3
    else:
        largest = val3
        if val1 >= val2:
            second_largest = val1
        else:
            second_largest = val2

    average = (largest + second_largest) / 2.0
    return average
    
    
    
    
def day_name(day_num):
    """
      -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """

    day = "Error"  # Default value is "Error"

    if day_num == 1:
        day = "Sunday"
    elif day_num == 2:
        day = "Monday"
    elif day_num == 3:
        day = "Tuesday"
    elif day_num == 4:
        day = "Wednesday"
    elif day_num == 5:
        day = "Thursday"
    elif day_num == 6:
        day = "Friday"
    elif day_num == 7:
        day = "Saturday"

    return day
    