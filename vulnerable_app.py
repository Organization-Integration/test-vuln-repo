import os
import sqlite3
import pickle
from flask import Flask, request

app = Flask(__name__)

# Hardcoded secret (security issue)
API_KEY = "12345-secret-api-key"


@app.route("/cmd")
def run_command():
    # Command Injection vulnerability
    user_input = request.args.get("cmd")
    os.system(user_input)
    return "Command executed"


@app.route("/user")
def get_user():
    # SQL Injection vulnerability
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()

    return {"data": str(result)}


@app.route("/load")
def load_data():
    # Unsafe deserialization vulnerability
    data = request.args.get("data")
    obj = pickle.loads(data.encode())
    return {"loaded": str(obj)}


@app.route("/read")
def read_file():
    # Path traversal vulnerability
    filename = request.args.get("file")
    with open(f"/var/data/{filename}", "r") as f:
        content = f.read()
    return {"content": content}


if __name__ == "__main__":
    app.run(debug=True)vulnerable_app.py
