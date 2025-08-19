# 代码生成时间: 2025-08-19 11:05:20
import requests
import json

class MessageNotificationSystem:
    """
    A simple message notification system using the Requests library to send HTTP requests.
    This system can be extended to support different notification methods such as email,
    web hooks, or other APIs.
    """

    def __init__(self, base_url):
        """
        Initialize the message notification system with a base URL.
        :param base_url: str - The base URL for sending notifications.
        """
        self.base_url = base_url

    def send_message(self, message, endpoint):
        """
        Send a message to a specified endpoint.
        :param message: str - The message to be sent.
        :param endpoint: str - The endpoint URL for the message.
        :return: dict - A dictionary containing the response from the server.
        """
        try:
            url = f"{self.base_url}{endpoint}"
            headers = {"Content-Type": "application/json"}
            payload = json.dumps({"message": message})
            response = requests.post(url, headers=headers, data=payload)
            return {"status_code": response.status_code, "response": response.json()}
        except requests.exceptions.RequestException as e:
            # Log the exception or handle it as needed
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    base_url = "https://api.example.com/notify"
    notification_system = MessageNotificationSystem(base_url)
    message = "Hello, this is a test notification."
    endpoint = "/test"
    result = notification_system.send_message(message, endpoint)
    print(json.dumps(result, indent=4))