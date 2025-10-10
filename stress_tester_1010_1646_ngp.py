# 代码生成时间: 2025-10-10 16:46:04
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException

"""
Stress Tester - A simple Python stress testing framework using the Requests library.

This script allows users to perform stress testing on a specified URL by sending a
large number of HTTP requests in a short amount of time.
"""

class StressTester:
    def __init__(self, url, num_requests, num_threads):
        """
        Initialize the StressTester with the target URL, number of requests, and number of threads.
        :param url: The URL to send requests to.
        :param num_requests: The total number of requests to send.
        :param num_threads: The number of concurrent threads to use.
        """
        self.url = url
        self.num_requests = num_requests
        self.num_threads = num_threads
        self.session = requests.Session()

    def send_request(self):
        """
        Send a single HTTP GET request to the target URL.
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.status_code
        except RequestException as e:
            print(f"Error sending request: {e}")
            return None

    def run(self):
        """
        Run the stress test using a ThreadPoolExecutor.
        """
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = [executor.submit(self.send_request) for _ in range(self.num_requests)]
            for future in futures:
                status_code = future.result()
                if status_code is not None:
                    print(f"Request succeeded with status code: {status_code}")

    def __str__(self):
        """
        Return a string representation of the StressTester instance.
        """
        return f"StressTester(url={self.url}, num_requests={self.num_requests}, num_threads={self.num_threads})"


def main():
    """
    Main function to run the stress test.
    """
    url = "http://example.com"  # Replace with the target URL
    num_requests = 100  # Number of requests to send
    num_threads = 10  # Number of concurrent threads to use
    stress_tester = StressTester(url, num_requests, num_threads)
    print(stress_tester)
    start_time = time.time()
    stress_tester.run()
    end_time = time.time()
    print(f"Stress test completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    main()