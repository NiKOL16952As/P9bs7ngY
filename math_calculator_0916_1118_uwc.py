# 代码生成时间: 2025-09-16 11:18:20
import requests

"""
Math Calculator Tool

This module provides a set of mathematical operations that can be performed using a remote API.
It includes addition, subtraction, multiplication, and division.
"""

class MathCalculator:
    # API endpoint for the math operations
    API_ENDPOINT = "https://api.mathjs.org/v4/"
    
    def __init__(self):
        """Initialize the MathCalculator with the API endpoint."""
        self.session = requests.Session()

    def add(self, a, b):
        """Perform addition operation.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the addition.
        """
        try:
            response = self.session.get(self.API_ENDPOINT, params={'a': a, 'b': b, 'operation': 'add'})
            response.raise_for_status()
            return response.json()['result']
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def subtract(self, a, b):
        """Perform subtraction operation.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the subtraction.
        """
        try:
            response = self.session.get(self.API_ENDPOINT, params={'a': a, 'b': b, 'operation': 'subtract'})
            response.raise_for_status()
            return response.json()['result']
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def multiply(self, a, b):
        """Perform multiplication operation.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The result of the multiplication.
        """
        try:
            response = self.session.get(self.API_ENDPOINT, params={'a': a, 'b': b, 'operation': 'multiply'})
            response.raise_for_status()
            return response.json()['result']
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def divide(self, a, b):
        """Perform division operation.

        Args:
            a (float): The numerator.
            b (float): The denominator.

        Returns:
            float: The result of the division.
        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        try:
            response = self.session.get(self.API_ENDPOINT, params={'a': a, 'b': b, 'operation': 'divide'})
            response.raise_for_status()
            return response.json()['result']
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Example usage:
if __name__ == '__main__':
    calculator = MathCalculator()
    print("Addition: 5 + 3 =", calculator.add(5, 3))
    print("Subtraction: 5 - 3 =", calculator.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calculator.multiply(5, 3))
    try:
        print("Division: 5 / 3 =", calculator.divide(5, 3))
    except ZeroDivisionError as e:
        print(e)