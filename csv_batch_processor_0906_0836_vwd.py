# 代码生成时间: 2025-09-06 08:36:19
import csv
import requests
from pathlib import Path

class CSVBatchProcessor:
    """
    A class to process CSV files in batches using the REQUESTS library.
    """
    def __init__(self, url, batch_size=100):
        """
        Initialize the CSVBatchProcessor with the target URL and batch size.
        :param url: The URL to send batches of CSV data to.
        :param batch_size: The number of records to send in each batch.
        """
        self.url = url
        self.batch_size = batch_size

    def process_csv(self, file_path):
        """
        Process a CSV file and send batches of data to the specified URL.
        :param file_path: The path to the CSV file to process.
        """
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row

                # Process the file in batches
                for i in range(0, sum(1 for row in reader), self.batch_size):
                    batch = list(reader)[:self.batch_size]
                    if batch:
                        self.send_batch(batch)

        except FileNotFoundError:
            print(f"Error: The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def send_batch(self, batch):
        """
        Send a batch of CSV data to the specified URL.
        :param batch: A list of rows from the CSV file.
        """
        try:
            # Convert the batch to a CSV string
            csv_string = '\
'.join([','.join(map(str, row)) for row in batch])
            
            # Send the batch via POST request
            response = requests.post(self.url, data=csv_string)
            
            # Check if the request was successful
            response.raise_for_status()
            print(f"Batch sent successfully. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred while sending the batch: {e}")

# Example usage:
# processor = CSVBatchProcessor("https://example.com/api/batch")
# processor.process_csv("data.csv")