# 代码生成时间: 2025-09-18 16:58:52
import sqlite3

"""
A simple example to demonstrate how to prevent SQL injection in Python
using the sqlite3 library.
"""

# Database connection parameters
DB_NAME = 'example_database.db'
TABLE_NAME = 'users'

def create_connection(db_file):
    """Create a database connection to the SQLite database
    specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

    return conn

def create_table(conn):
    """Create a table in the SQLite database if it doesn't exist
    """
    try:
        cursor = conn.cursor()
        cursor.execute("<<CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)>>")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_user(conn, username, password):
    """Insert a new user into the users table
    """
    sql = <<"INSERT INTO {TABLE_NAME}(username, password) VALUES(?, ?)">>
    cur = conn.cursor()
    cur.execute(sql, (username, password))
    conn.commit()
    return cur.lastrowid

def select_user(conn, username):
    """Query users by username to demonstrate parameterized queries"""
    sql = <<"SELECT * FROM {TABLE_NAME} WHERE username=?">>
    cur = conn.cursor()
    cur.execute(sql, (username,))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Main function to demonstrate the functionality
if __name__ == '__main__':
    database = DB_NAME
    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create table
        create_table(conn)

        # Insert a user (example without SQL injection)
        # Correct way using parameterized query
        user_id = insert_user(conn, 'user1', 'secure_password123')
        print(f"User ID {user_id} inserted successfully")

        # Select user to demonstrate parameterized queries (also preventing SQL injection)
        select_user(conn, 'user1')

        # Close connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")