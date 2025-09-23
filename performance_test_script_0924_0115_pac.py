# 代码生成时间: 2025-09-24 01:15:37
import requests
import time
from requests.exceptions import RequestException
from urllib.parse import urljoin

"""
A simple performance testing script that sends HTTP requests to a specified URL
and measures the response time.
"""

class PerformanceTest:
    def __init__(self, base_url):
        """
        Initializes the PerformanceTest object with the base URL.
        :param base_url: The base URL to which the requests will be sent.
        """
        self.base_url = base_url
        self.endpoints = []

    def add_endpoint(self, endpoint):
        """
        Adds an endpoint to the test.
        :param endpoint: The endpoint to be added.
        """
        self.endpoints.append(urljoin(self.base_url, endpoint))

    def run_test(self, num_requests=10):
        """
        Runs the performance test.
        :param num_requests: The number of requests to send to each endpoint.
        """
        start_time = time.time()
        for endpoint in self.endpoints:
            for _ in range(num_requests):
                try:
                    response = requests.get(endpoint)
                    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
                except RequestException as e:
                    print(f"An error occurred: {e}")
                    continue
        end_time = time.time()
        print(f"Total time for {len(self.endpoints)} endpoints with {num_requests} requests each: {end_time - start_time} seconds")

# Example usage
if __name__ == '__main__':
    base_url = 'http://example.com'
    test = PerformanceTest(base_url)
    test.add_endpoint('/path/to/endpoint1')
    test.add_endpoint('/path/to/endpoint2')
    test.run_test(num_requests=100)  # Sends 100 requests to each endpoint.
