# 代码生成时间: 2025-08-17 05:17:53
import requests

"""
Sorting Algorithm implementation using Python and the Requests framework.
This module provides a simple sorting function to sort a list of numbers.

Attributes:
    None

Methods:
    sort_numbers(numbers): Sorts a list of numbers in ascending order.
"""


def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.
    
    Args:
        numbers (list): A list of numbers to be sorted.
    
    Returns:
        list: The sorted list of numbers.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("List must contain only numeric values.")
    
    sorted_numbers = sorted(numbers)
    return sorted_numbers

# Example usage
if __name__ == '__main__':
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    try:
        sorted_list = sort_numbers(numbers)
        print("Sorted numbers:", sorted_list)
    except (TypeError, ValueError) as e:
        print("Error: ", e)