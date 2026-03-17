"""
Module containing the two functions used in the resistor color problem
"""

resistors = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
     "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def color_code(color):
    """
    This function returns the value of the resistor associated with the color key
    """
    for key, value in resistors.items():
        if key == color:
            return value
    return None


def colors():
    """
    This function returns the list of possible colors of the resistors
    """
    return list(resistors.keys())