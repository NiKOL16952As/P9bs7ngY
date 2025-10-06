# 代码生成时间: 2025-10-06 19:39:46
import requests
from requests.exceptions import HTTPError
import json

class SentimentAnalysisTool:
    """
    A simple sentiment analysis tool using a third-party API.
    This class encapsulates the functionality to send text to an API and
    receive sentiment analysis results.
    """

    def __init__(self, api_url):
        """
        Initialize the SentimentAnalysisTool with the API URL.
        :param api_url: The URL of the sentiment analysis API.
        """
        self.api_url = api_url

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of the provided text.
        :param text: The text to be analyzed.
        :return: A dictionary containing the sentiment analysis results.
        :raises: HTTPError if the API request fails.
        """
        try:
            response = requests.post(self.api_url, json={'text': text})
            response.raise_for_status()  # Raises HTTPError for 4XX or 5XX errors
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

# Example usage
if __name__ == '__main__':
    # Replace 'your_api_url' with the actual API URL provided by the sentiment analysis service.
    api_url = 'your_api_url'
    sentiment_tool = SentimentAnalysisTool(api_url)

    try:
        text_to_analyze = "This is a great day!"
        sentiment_result = sentiment_tool.analyze_sentiment(text_to_analyze)
        print("Sentiment Analysis Result:", sentiment_result)
    except Exception as e:
        print("Failed to perform sentiment analysis.", e)