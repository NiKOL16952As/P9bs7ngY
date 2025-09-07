# 代码生成时间: 2025-09-07 18:19:22
import requests
import subprocess
import sys
from typing import List, Tuple

"""
Process Manager

A simple process manager built using Python and the requests framework.
This module allows users to list, start, stop, and restart processes.
"""

class ProcessManager:
    """Class for managing processes."""
    def __init__(self, host: str = 'localhost', port: int = 8080):
        """Initialize the ProcessManager with the host and port."""
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"

    def list_processes(self) -> List[str]:
        """List all running processes."""
        url = f"{self.base_url}/processes"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error listing processes: {e}")
            return []

    def start_process(self, process_name: str) -> bool:
        """Start a new process with the given name."""
        url = f"{self.base_url}/processes/{process_name}/start"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error starting process {process_name}: {e}")
            return False

    def stop_process(self, process_name: str) -> bool:
        """Stop the process with the given name."""
        url = f"{self.base_url}/processes/{process_name}/stop"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error stopping process {process_name}: {e}")
            return False

    def restart_process(self, process_name: str) -> bool:
        """Restart the process with the given name."""
        url = f"{self.base_url}/processes/{process_name}/restart"
        try:
            response = requests.put(url)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error restarting process {process_name}: {e}")
            return False


def main():
    """Main function to interact with the process manager."""
    pm = ProcessManager()
    while True:
        print("1. List processes
2. Start process
3. Stop process
4. Restart process
5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            processes = pm.list_processes()
            print(f"Running processes: {processes}")
        elif choice == '2':
            process_name = input("Enter the process name to start: ")
            if pm.start_process(process_name):
                print(f"Process {process_name} started successfully.")
            else:
                print(f"Failed to start process {process_name}.")
        elif choice == '3':
            process_name = input("Enter the process name to stop: ")
            if pm.stop_process(process_name):
                print(f"Process {process_name} stopped successfully.")
            else:
                print(f"Failed to stop process {process_name}.")
        elif choice == '4':
            process_name = input("Enter the process name to restart: ")
            if pm.restart_process(process_name):
                print(f"Process {process_name} restarted successfully.")
            else:
                print(f"Failed to restart process {process_name}.")
        elif choice == '5':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()