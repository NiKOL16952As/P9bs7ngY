# 代码生成时间: 2025-08-18 16:49:21
import requests
from requests.exceptions import RequestException

"""
A simple message notification system that sends a notification to a specified URL.
"""

class MessageNotificationSystem:
    def __init__(self, notification_url):
        """
        Initializes the notification system with the URL to send notifications to.
        :param notification_url: The URL to send notifications to.
        """
        self.notification_url = notification_url

    def send_notification(self, message):
        """
        Sends a notification message to the specified URL.
        :param message: The message to send.
        :return: True if the notification was sent successfully, False otherwise.
        """
        try:
            # Prepare the notification data to be sent
            notification_data = {"message": message}
            # Send the POST request to the notification URL
            response = requests.post(self.notification_url, json=notification_data)
            # Check if the request was successful
            response.raise_for_status()
            return True
        except RequestException as e:
            # Log the error (for simplicity, just printing it here)
            print(f"Error sending notification: {e}")
            return False

    def __str__(self):
        """
        Returns a string representation of the notification system.
        """
        return f"MessageNotificationSystem(url={self.notification_url})"

# Example usage
if __name__ == "__main__":
    # Define the URL to send notifications to
    notification_url = "http://example.com/notify"
    # Create a new instance of the notification system
    notifier = MessageNotificationSystem(notification_url)
    # Send a test notification
    result = notifier.send_notification("Hello, this is a test notification!")
    # Print the result
    print(f"Notification sent: {result}")