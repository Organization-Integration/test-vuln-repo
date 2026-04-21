from flask import request
import sqlite3

def login():
    conn = sqlite3.connect("app.db")

    username = request.form["user"]
    password = request.form["pass"]

    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"

    conn.execute(query)
