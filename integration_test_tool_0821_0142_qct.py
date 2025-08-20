# 代码生成时间: 2025-08-21 01:42:50
import requests
import json
from typing import Dict, Any

"""
Integration Test Tool

This tool is designed to perform integration tests on APIs using the requests library.
"""

class APITest:
    def __init__(self, base_url: str, auth: Dict[str, str] = None):
        """Initialize the APITest instance.

        Args:
            base_url (str): The base URL of the API.
            auth (Dict[str, str], optional): Authentication credentials. Defaults to None.
        """
        self.base_url = base_url
        self.auth = auth

    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Perform a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            params (Dict[str, Any], optional): Query parameters. Defaults to None.

        Returns:
            Dict[str, Any]: The JSON response from the server.
        """
        try:
            response = requests.get(self.base_url + endpoint, params=params, auth=self.auth)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

    def post(self, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Perform a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            data (Dict[str, Any], optional): Data to be sent in the request body. Defaults to None.

        Returns:
            Dict[str, Any]: The JSON response from the server.
        """
        try:
            response = requests.post(self.base_url + endpoint, json=data, auth=self.auth)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    # Define the base URL and authentication credentials
    base_url = "https://api.example.com"
    auth = {"username": "user", "password": "pass"}

    # Create an instance of APITest
    test = APITest(base_url, auth)

    # Perform a GET request
    response_get = test.get("/endpoint")
    print("GET Response:", response_get)

    # Perform a POST request
    response_post = test.post("/endpoint", {"key": "value"})
    print("POST Response: