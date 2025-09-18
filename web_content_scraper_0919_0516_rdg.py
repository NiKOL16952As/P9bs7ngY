# 代码生成时间: 2025-09-19 05:16:15
import requests
from bs4 import BeautifulSoup
import logging

"""
Web Content Scraper

This module provides a simple web content scraping tool using Python and Requests framework.
It fetches content from a given URL and parses it using BeautifulSoup.
"""

class WebContentScraper:
    def __init__(self, url):
        """
        Initialize the WebContentScraper instance with a URL
        :param url: The URL to scrape content from
        """
        self.url = url
        self.session = requests.Session()

    def fetch_content(self):
        """
        Fetch the content from the given URL
        :return: The HTML content of the webpage as a string
        :raises: requests.RequestException if the request fails
        """
        try:
            response = self.session.get(self.url)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            return response.text
        except requests.RequestException as e:
            logging.error(f"Failed to fetch content from {self.url}: {e}")
            raise

    def parse_content(self, html_content):
        """
        Parse the HTML content using BeautifulSoup
        :param html_content: The HTML content of the webpage as a string
        :return: The parsed content as a BeautifulSoup object
        """
        return BeautifulSoup(html_content, 'html.parser')

    def scrape(self):
        """
        Scrape the content from the given URL
        :return: The parsed content as a BeautifulSoup object
        """
        try:
            html_content = self.fetch_content()
            parsed_content = self.parse_content(html_content)
            return parsed_content
        except Exception as e:
            logging.error(f"Failed to scrape content from {self.url}: {e}")
            raise

# Example usage
if __name__ == '__main__':
    url = 'http://example.com'
    scraper = WebContentScraper(url)
    try:
        content = scraper.scrape()
        print(content.prettify())
    except Exception as e:
        logging.error(f"Error scraping content from {url}: {e}")