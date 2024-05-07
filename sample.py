# example.py
import sqlite3

def insecure_login():
    username = input("Enter your username: ")
    # Hardcoded password (Security Risk)
    password = "secretPassword123"
    
    # Connection to a SQLite database
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Unsafe SQL query susceptible to SQL Injection (Security Risk)
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    c.execute(query)
    results = c.fetchall()

    if results:
        print("Logged in successfully!")
    else:
        print("Failed to log in.")
    conn.close()

if __name__ == "__main__":
    insecure_login()
