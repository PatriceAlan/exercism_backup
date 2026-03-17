"""
Module implementing the solution to the raindrops problem
"""

def convert(number):
    """
    Function converting a number to a string according to some conditions
    """
    sound = ""
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    if sound == "":
        sound += str(number)
    return sound
        
