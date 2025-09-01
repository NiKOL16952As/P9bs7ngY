# 代码生成时间: 2025-09-01 19:42:20
import requests
from bs4 import BeautifulSoup

"""
A simple web scraper tool that fetches the content of a webpage.

Usage:
    python web_scraper.py <URL>

This script will print the fetched HTML content.

Attributes:
    - url (str): The URL of the webpage to scrape.

Methods:
    - fetch_content(url): Fetches the webpage content.
    - parse_html(content): Parses the HTML content using BeautifulSoup.

Example:
    >>> fetch_content('https://example.com')
    >>> html_content = parse_html(response.content)
    >>> print(html_content.prettify())
"""


def fetch_content(url):
    """
    Fetches the content of the webpage located at the given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        response: The response object from the requests library.

    Raises:
        requests.RequestException: If there is a problem with the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def parse_html(content):
    """
    Parses the HTML content using BeautifulSoup.

    Args:
        content (bytes): The HTML content to parse.

    Returns:
        soup: The parsed HTML as a BeautifulSoup object.
    """
    soup = BeautifulSoup(content, 'html.parser')
    return soup


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python web_scraper.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    response = fetch_content(url)
    if response:
        html_content = parse_html(response.content)
        print(html_content.prettify())