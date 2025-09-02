# 代码生成时间: 2025-09-02 19:54:03
import requests
from bs4 import BeautifulSoup
import os

"""
A Python script to demonstrate how to use the REQUESTS library to fetch and process webpages
for responsive layout design. This script will fetch a webpage and extract relevant
HTML elements to check if they adapt to different screen sizes."""

def fetch_webpage(url):
    """
    Fetches the content of the webpage from the given URL.
    
    Args:
    url (str): The URL of the webpage to fetch.
    
    Returns:
    str: The HTML content of the webpage.
    
    Raises:
    requests.RequestException: If there is an issue with the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return None

def parse_html(html_content):
    """
    Parses the HTML content to find elements that are part of a responsive design.
    
    Args:
    html_content (str): The HTML content of the webpage.
    
    Returns:
    list: A list of tuples containing the element tag and its class attribute.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    responsive_elements = []
    for element in soup.find_all(class_=lambda x: x and 'responsive' in x):
        responsive_elements.append((element.name, element.get('class')))
    return responsive_elements

def main():
    """
    The main function to fetch a webpage and check for responsive elements.
    """
    url = 'https://example.com'  # Replace with the URL you want to check
    html_content = fetch_webpage(url)
    if html_content:
        responsive_elements = parse_html(html_content)
        print("Responsive elements found: ")
        for element in responsive_elements:
            print(element)
    else:
        print("Failed to fetch webpage.")

if __name__ == '__main__':
    main()