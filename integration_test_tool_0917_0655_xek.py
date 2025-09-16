# 代码生成时间: 2025-09-17 06:55:49
import requests
import json

class IntegrationTestTool:
    """
    Integration test tool for making HTTP requests and testing responses.

    Attributes:
        base_url (str): The base URL for the API being tested.
        tests (list): A list of test cases to be executed.
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.tests = []

    def add_test(self, endpoint, method, expected_status, expected_response):
        """
        Add a test case to the list of tests.

        Args:
            endpoint (str): The endpoint to be tested.
            method (str): The HTTP method to use (e.g., 'GET', 'POST').
            expected_status (int): The expected HTTP status code.
            expected_response (dict): The expected response body.
        """
        self.tests.append((endpoint, method, expected_status, expected_response))

    def run_tests(self):
        """
        Run all the tests and print the results.
        """
        for test in self.tests:
            endpoint, method, expected_status, expected_response = test
            url = f"{self.base_url}{endpoint}"
            try:
                response = requests.request(method, url)
                if response.status_code == expected_status:
                    print(f"Test {endpoint} passed: Status {response.status_code}")
                    self._validate_response(response.json(), expected_response)
                else:
                    print(f"Test {endpoint} failed: Expected status {expected_status}, got {response.status_code}")
            except requests.RequestException as e:
                print(f"Test {endpoint} failed: {e}")

    def _validate_response(self, actual_response, expected_response):
        """
        Validate the actual response against the expected response.

        Args:
            actual_response (dict): The actual response body.
            expected_response (dict): The expected response body.
        """
        if actual_response != expected_response:
            print("Response validation failed.")
            print("Expected: ", json.dumps(expected_response, indent=4))
            print("Actual: ", json.dumps(actual_response, indent=4))
        else:
            print("Response validation passed.")

# Example usage
if __name__ == '__main__':
    base_url = 'http://example.com/api/'
    test_tool = IntegrationTestTool(base_url)

    # Add test cases
    test_tool.add_test('/users', 'GET', 200, {'success': True, 'users': []})
    test_tool.add_test('/users', 'POST', 201, {'success': True, 'user_id': 1})

    # Run tests
    test_tool.run_tests()