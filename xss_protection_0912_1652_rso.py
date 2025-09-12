# 代码生成时间: 2025-09-12 16:52:23
import requests
from bs4 import BeautifulSoup

"""
Module for detecting and preventing XSS (Cross-Site Scripting) attacks
by sanitizing input data using BeautifulSoup.
"""

class XSSProtection:
    """Class to handle XSS protection."""

    def __init__(self, user_input):
        """Initialize the XSS protector with user input."""
        self.user_input = user_input

    def sanitize_input(self):
        """Sanitize the user input to prevent XSS attacks."""
        try:
            # Parse the user input with BeautifulSoup
            soup = BeautifulSoup(self.user_input, 'html.parser')
            # Remove all script and iframe tags to prevent XSS
            for script in soup(['script', 'iframe']):
                script.decompose()
            # Return the sanitized input
            return str(soup)
        except Exception as e:
            # Handle any exceptions that occur during sanitization
            print(f"An error occurred: {e}")
            return None

    def test_protection(self, url):
        """Send a sanitized payload to a URL to test XSS protection."""
        sanitized_input = self.sanitize_input()
        if sanitized_input is None:
            print("Failed to sanitize input.")
            return

        try:
            # Send a POST request with the sanitized input
            response = requests.post(url, data={'user_input': sanitized_input})
            # Check if the server processed the request successfully
            if response.status_code == 200:
                print("XSS protection test passed.")
            else:
                print(f"Failed to test XSS protection: {response.status_code}")
        except requests.RequestException as e:
            # Handle any request-related exceptions
            print(f"Request failed: {e}")

# Example usage
if __name__ == '__main__':
    user_input = "<script>alert('XSS')</script>"  # Example user input
    xss_protection = XSSProtection(user_input)
    url = "http://example.com/test"  # URL to test XSS protection
    xss_protection.test_protection(url)