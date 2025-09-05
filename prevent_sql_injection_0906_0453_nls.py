# 代码生成时间: 2025-09-06 04:53:52
import sqlite3

"""
This module demonstrates how to prevent SQL injection by using parameterized queries.
It creates a simple database with a table for demonstration purposes and performs
safe queries to retrieve and insert data.
"""

class Database:
    def __init__(self, db_name):
        """ Initialize the database connection. """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """ Create a table for demonstration. """
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL
            );"""
        )
        self.connection.commit()

    def insert_user(self, username, email):
        """ Insert a new user into the database using parameterized queries. """
        try:
            self.cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def get_user(self, username):
        """ Retrieve a user's details from the database using a parameterized query. """
        try:
            self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        """ Close the database connection. """
        self.connection.close()

# Example usage
if __name__ == '__main__':
    # Initialize the database
    db = Database('example.db')

    # Insert a user (safe from SQL injection)
    db.insert_user('john_doe', 'john@example.com')

    # Retrieve a user (safe from SQL injection)
    user = db.get_user('john_doe')
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

    # Close the database connection
    db.close()