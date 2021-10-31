import math


def add_and_subtract(a, b, c, d):
    """Function to return the sum of the first 2 inputs minus the 2 of the last 2 inputs."""
    
    result = (a + b) - (c + d)

    return result


def square(a):
    """Function to square the input."""

    return a**2


def log_10(a):
    """Function to return the log base 10 of the input."""

    return math.log10(a)


def sum_list(list_to_sum):
    """Function to sum the items in the input list."""

    return sum(list_to_sum)


def check_string_type(possible_string):
    """Function to return 1 if the input is a string otherwise raise a TypeError."""

    if type(possible_string) is str:

        return 1

    else:

        raise TypeError(f'string not passed - got type {type(possible_string)})')


def long_string(potentially_long_string):
    """Function to return the input string if has at least 10 characters."""

    if len(potentially_long_string) >= 10:

        return potentially_long_string


def string_contrains_substring(str1, str2):
    """Function to return True if str1 contains str2 otherwise return False."""

    if str1.find(str2) >= 0:

        return True
    
    else:

        return False


def print_int_string(int_value, string_value):
    """Function to print string value, int_value times."""

    for _ in range(int_value):

        print(string_value)


