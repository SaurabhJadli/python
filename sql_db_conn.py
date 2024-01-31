import sys; sys.executable
import mysql.connector

# Replace these values with your MySQL connection details
config = {
    'user': 'root',
    'password': 'iamsuu7',
    'host': 'localhost',
    'database': 'university',
    'raise_on_warnings': True,
}

# Establish a connection
try:
    conn = mysql.connector.connect(**config)
    print("Connected to MySQL!")
    # Perform operations here
    # ...
    conn.close()  # Close the connection when done
except mysql.connector.Error as err:
    print(f"Error: {err}")
