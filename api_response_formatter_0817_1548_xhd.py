# 代码生成时间: 2025-08-17 15:48:19
import requests
import json

class ApiResponseFormatter:
    """
    A utility class to format API responses.

    This class provides methods to send requests to an API and format the response in a user-friendly way.
    """

    def __init__(self, base_url):
        """Initialize the class with a base URL for the API."""
        self.base_url = base_url

    def send_request(self, endpoint, method='GET', data=None, headers=None):
        """Send a request to the specified API endpoint."""
        url = self.base_url + endpoint
        try:
            response = requests.request(method, url, data=data, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP error codes
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {'error': f'HTTP error occurred: {http_err}'}
        except requests.exceptions.RequestException as err:
            return {'error': f'Error occurred: {err}'}
        except Exception as e:
            return {'error': f'An unexpected error occurred: {e}'}

    def format_response(self, response_data):
        """Format the API response data."""
        # Placeholder for response formatting logic, can be customized based on specific needs
        formatted_response = {
            'status': 'success',
            'data': response_data
        }
        return formatted_response

# Example usage
if __name__ == '__main__':
    base_url = 'https://api.example.com/'
    formatter = ApiResponseFormatter(base_url)
    endpoint = 'users'
    method = 'GET'

    response_data = formatter.send_request(endpoint, method)
    if 'error' not in response_data:
        formatted_response = formatter.format_response(response_data)
        print(json.dumps(formatted_response, indent=4))
    else:
        print(response_data['error'])