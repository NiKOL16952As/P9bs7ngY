# 代码生成时间: 2025-08-30 21:57:31
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='security_audit.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityAuditLogger:
    def __init__(self, url):
        """
        Initializes the Security Audit Logger with the given URL to which the logs will be sent.
        The URL should be the endpoint of the server that will process the audit logs.
        """
        self.url = url

    def log_event(self, event_type, message, user_info=None):
        try:
            """
            Logs an event to the security audit log.
            Sends the log to the server if the url is specified.
            """
            # Compose the log entry
            log_entry = {
                'event_type': event_type,
                'message': message,
                'timestamp': datetime.utcnow().isoformat(),
                'user_info': user_info
            }

            # Send the log entry to the server
            response = requests.post(self.url, json=log_entry)
            response.raise_for_status()

            # Log locally
            logging.info(f'Logged event: {log_entry}')

        except requests.RequestException as e:
            # If there's an error sending the log, log the error locally
            logging.error(f'Failed to send log to server: {e}')
        except Exception as e:
            # General error handling for any other exceptions
            logging.error(f'An error occurred while logging event: {e}')

# Example usage
if __name__ == '__main__':
    # Initialize the logger with the server URL
    audit_logger = SecurityAuditLogger('https://example.com/audit_log_endpoint')

    # Log an example event
    audit_logger.log_event('USER_LOGIN', 'User attempted to login to the system.', user_info='username')
