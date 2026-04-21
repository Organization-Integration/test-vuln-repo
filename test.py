import os
import subprocess
import pickle

# 1. Hardcoded secrets (multiple findings)
password = "admin123"
api_key = "secret-key"
token = "12345"

# 2. Unsafe command execution (hotspot)
user_input = input("Enter command: ")
os.system(user_input)

# 3. Subprocess with shell=True (strong signal)
subprocess.call("ls " + user_input, shell=True)

# 4. Dangerous eval (hotspot)
eval(user_input)

# 5. Unsafe deserialization (important)
data = pickle.loads(b"malicious data")

# 6. Weak randomness
import random
random_value = random.random()

# 7. Debug code (code smell)
print("debug:", password)
