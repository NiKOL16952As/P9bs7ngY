# 代码生成时间: 2025-08-11 12:23:09
import requests
import socket
from requests.exceptions import ConnectionError, Timeout, RequestException

"""
Network Connection Checker
This script checks the network connection status by attempting to reach a list of URLs.

Attributes:
    None

Methods:
    check_connection(url): Checks if the URL is reachable.
    main(urls): Main method to check connection status for a list of URLs.
"""

def check_connection(url):
    """
    Checks if the provided URL is reachable.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is reachable, False otherwise.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return True
    except (ConnectionError, Timeout, RequestException):
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main(urls):
    """
    Main method to check connection status for a list of URLs.

    Args:
        urls (list): A list of URLs to check.
    """
    for url in urls:
        status = check_connection(url)
        print(f"URL: {url} is {'reachable' if status else 'not reachable'}")

if __name__ == '__main__':
    # URLs to check
    urls_to_check = [
        'http://www.google.com',
        'http://www.bing.com',
        'http://www.stackoverflow.com'
    ]
    
    main(urls_to_check)