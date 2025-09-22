# 代码生成时间: 2025-09-22 14:57:45
import psutil
import requests
from datetime import datetime

"""
Memory Usage Analyzer

This module analyzes the memory usage of the system. It provides an API to retrieve
system memory usage statistics and optionally, if connected to a server,
can retrieve the memory usage statistics of other systems connected to the network.
"""

class MemoryAnalyzer:
    def __init__(self, server_url=None):
        """Initialize the MemoryAnalyzer class.

        Args:
            server_url (str, optional): The URL of the server to fetch memory usage data from. Defaults to None.
        """
        self.server_url = server_url

    def get_local_memory_usage(self):
        """Get the memory usage statistics for the local system.

        Returns:
            dict: A dictionary containing memory usage data.
        """
        try:
            memory = psutil.virtual_memory()
            return {
                'available': memory.available,
                'used': memory.used,
                'percent': memory.percent,
                'total': memory.total
            }
        except Exception as e:
            raise RuntimeError("Failed to get local memory usage: " + str(e))

    def get_remote_memory_usage(self):
        """Get the memory usage statistics for remote systems.

        Returns:
            dict: A dictionary containing memory usage data for remote systems.
        """
        if self.server_url is None:
            raise ValueError("Server URL is not provided.")

        try:
            response = requests.get(self.server_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ConnectionError("Failed to connect to server: " + str(e))

    def analyze_memory_usage(self):
        """Analyze and print memory usage statistics.

        If a server URL is provided, retrieve and print memory usage from remote systems as well.
        """
        print("Local Memory Usage: ")
        local_usage = self.get_local_memory_usage()
        print(local_usage)

        if self.server_url:
            print("Remote Memory Usage: ")
            remote_usage = self.get_remote_memory_usage()
            print(remote_usage)

# Example usage
if __name__ == '__main__':
    analyzer = MemoryAnalyzer("http://example.com/memory_usage")
    try:
        analyzer.analyze_memory_usage()
    except Exception as e:
        print("Error: " + str(e))
