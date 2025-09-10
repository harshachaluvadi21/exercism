"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # The total expected bake time in minutes
PREPARATION_TIME_PER_LAYER = 2  # Preparation time per layer in minutes


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the total preparation time based on the number of layers.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed time (preparation + baking).

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
