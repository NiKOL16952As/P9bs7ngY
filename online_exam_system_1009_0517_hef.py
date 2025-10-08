# 代码生成时间: 2025-10-09 05:17:34
import requests

"""
Online Exam System using the requests framework in Python.
This script simulates a basic online exam system where questions are
fetched from a remote API and answers are sent back.
"""

# Constants
API_URL = "http://example.com/api/questions"
SUBMIT_URL = "http://example.com/api/submit"

# Main function to simulate the exam
def main():
    try:
        # Fetch the questions from the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Process the response
        questions = response.json()
        print("Here are your questions:"\)
        for question in questions:
            print(f"{question['id']}. {question['text']}")
            answer = input("Enter your answer (ID): ")
            # Submit the answer to the API
            submit_response = requests.post(SUBMIT_URL, json={'question_id': question['id'], 'answer': answer})
            submit_response.raise_for_status()
            
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Invalid response from the server.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()