# 代码生成时间: 2025-09-23 13:38:35
import requests
import time
from concurrent.futures import ThreadPoolExecutor

"""
Performance testing script using Python and Requests Library.
This script sends a specified number of requests to a given URL and measures the response time.
"""

class PerformanceTest:
    def __init__(self, url, num_requests, concurrency_level):
        """
        Initialize the performance test with the given URL, number of requests, and concurrency level.
        :param url: The URL to test, as a string.
        :param num_requests: The number of requests to send, as an integer.
        :param concurrency_level: The number of concurrent requests, as an integer.
        """
        self.url = url
        self.num_requests = num_requests
        self.concurrency_level = concurrency_level
        self.timings = []

    def send_request(self):
        """
        Send a single request to the URL and record the response time.
        """
        try:
            start_time = time.time()
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            end_time = time.time()
            self.timings.append(end_time - start_time)
        except requests.RequestException as e:
            print(f"Request failed: {e}")

    def run_test(self):
        """
        Run the performance test by sending concurrent requests.
        """
        with ThreadPoolExecutor(max_workers=self.concurrency_level) as executor:
            futures = [executor.submit(self.send_request) for _ in range(self.num_requests)]
            for future in futures:
                future.result()  # Retrieves the result and raises exceptions if any

    def report(self):
        """
        Generate and print a report of the performance test results.
        """
        if not self.timings:
            print("No data to report.")
            return
        total_time = sum(self.timings)
        average_time = total_time / len(self.timings)
        print(f"Total time: {total_time:.2f} seconds")
        print(f"Average time per request: {average_time:.2f} seconds")
        print(f"Number of requests: {len(self.timings)}")

# Example usage
if __name__ == "__main__":
    URL = "http://example.com"
    NUM_REQUESTS = 100
    CONCURRENCY_LEVEL = 10

    test = PerformanceTest(URL, NUM_REQUESTS, CONCURRENCY_LEVEL)
    test.run_test()
    test.report()