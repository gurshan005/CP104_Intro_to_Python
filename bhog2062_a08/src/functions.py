"""
-------------------------------------------------------
[ASSIGNMENT 8, functions]
-------------------------------------------------------
Author:  gurshan bhogal 
ID:      169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2023-10-11"
-------------------------------------------------------
"""

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    
    if not sentence:
        return ""

    spaced = sentence[0]  # Initialize the result with the first character

    for char in sentence[1:]:
        if char.isupper():
            spaced += " " + char.lower()  # Add a space before uppercase characters and convert to lowercase
        else:
            spaced += char

    return spaced

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    
    if string.endswith(('s', 'sh', 'ch')):
        pluralized = string + 'es'
    elif string.endswith('y') and not string.endswith(('ay', 'oy')):
        pluralized = string[:-1] + 'ies'
    else:
        pluralized = string + 's'
    
    return pluralized
    
def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    
    len_str1 = len(str1)
    len_str2 = len(str2)

    suffix = ""

    # Start from the end of both strings and compare characters
    i = 1
    while i <= min(len_str1, len_str2) and str1[-i] == str2[-i]:
        suffix = str1[-i] + suffix
        i += 1

    return suffix

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """ 
    # Check if the ISBN has the correct length
    if len(isbn) != 17:
        return False

    # Check if the ISBN consists of only digits and dashes
    if not isbn.replace("-", "").isdigit():
        return False

    # Check if the ISBN has 5 groups of digits separated by dashes
    groups = isbn.split("-")
    if len(groups) != 5:
        return False

    # Check if the first group of digits is either '978' or '979'
    if groups[0] not in {'978', '979'}:
        return False

    # Check if the final group of digits is a single digit
    if len(groups[-1]) != 1 or not groups[-1].isdigit():
        return False
    
    if '--' in isbn:
        return False


    return True


def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(words) < 2:
        return False

    # Use all() and a generator expression to check the word chain condition
    return all(words[i][-1] == words[i + 1][0] for i in range(len(words) - 1))

    
 
 
    
    