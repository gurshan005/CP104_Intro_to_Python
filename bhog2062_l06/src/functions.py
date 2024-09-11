def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """ 
    
    total = 0
    for i in range(2, num + 1, 2):
        total += i
    return total
    
    
def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """ 
    
    for i in range(height):
        if i == 0 or i == height - 1:
            # Print the top and bottom rows with the given character
            print(char * width)
        else:
            # Print the sides with characters in between
            middle_chars = char * (width - 2)
            print(char + middle_chars + char)

            
def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    
  

    for time in range(start, end + 1, inc):
        calories_burnt = burnt_per_minute * time
        print(f"Calories burned after {time} minutes: {calories_burnt:.1f}")
        
        
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    
    if n <= 0:
        raise ValueError("n must be greater than 0")

    total = 0
    minimum = None
    maximum = None

    for i in range(n):
        value = float(input(f"Enter Value {i+1}: "))
        total += value

        if minimum is None or value < minimum:
            minimum = value

        if maximum is None or value > maximum:
            maximum = value

    average = total / n

    return minimum, maximum, total, average
        
def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    song = ""
    for i in range(n, 0, -1):
        song += f"{i} {'bottle' if i == 1 else 'bottles'} of beer on the wall, {i} {'bottle' if i == 1 else 'bottles'} of beer.\n"
        song += f"Take one down, pass it around, {i - 1 if i > 1 else 'no more'} {'bottle' if i == 2 else 'bottles'} of beer on the wall!\n--\n"
    print(song)
    return None
        
    