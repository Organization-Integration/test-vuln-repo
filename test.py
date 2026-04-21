import os
import sqlite3
import subprocess
import pickle
import random
import jwt
from flask import request

# -------------------------
# 1. Hardcoded credentials (Issue)
# -------------------------
password = "admin123"
api_key = "secret-key"

# -------------------------
# 2. JWT secret exposure (Blocker)
# -------------------------
JWT_SECRET = "super-secret-key"
token = jwt.encode({"user": "admin"}, JWT_SECRET, algorithm="HS256")

# -------------------------
# 3. SQL Injection (Blocker - S3649)
# -------------------------
def sql_injection():
    conn = sqlite3.connect("test.db")
    username = request.args.get("user")  # user input
    query = f"SELECT * FROM users WHERE name = '{username}'"
    conn.execute(query)

# -------------------------
# 4. Command Injection (Hotspot)
# -------------------------
def command_injection():
    cmd = request.args.get("cmd")
    os.system(cmd)

# -------------------------
# 5. Subprocess shell=True (Hotspot)
# -------------------------
def subprocess_issue():
    cmd = request.args.get("cmd")
    subprocess.call("ls " + cmd, shell=True)

# -------------------------
# 6. Dangerous eval (Hotspot)
# -------------------------
def eval_issue():
    data = request.args.get("data")
    eval(data)

# -------------------------
# 7. Unsafe deserialization (Hotspot)
# -------------------------
def deserialization_issue():
    data = request.data
    pickle.loads(data)

# -------------------------
# 8. Weak randomness (Issue)
# -------------------------
def weak_random():
    return random.random()

# -------------------------
# 9. Debug print (Code smell)
# -------------------------
print("Debug password:", password)
