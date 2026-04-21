import sqlite3

def get_user(username):
    conn = sqlite3.connect("test.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"  # SQLi
    return conn.execute(query).fetchall()
