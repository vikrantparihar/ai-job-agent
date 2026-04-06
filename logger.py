import os
from datetime import datetime

if not os.path.exists("logs"):
    os.makedirs("logs")

def log_info(msg):
    write_log("INFO", msg)

def log_error(msg):
    write_log("ERROR", msg)

def write_log(level, msg):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] [{level}] {msg}"

    print(line)

    with open("logs/app.log", "a") as f:
        f.write(line + "\n")