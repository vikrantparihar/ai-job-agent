import sqlite3

jobs = [
    "https://www.linkedin.com/jobs/view/4380075354/",
    "https://www.linkedin.com/jobs/view/4394425141/",
    "https://www.linkedin.com/jobs/view/4382579105/"
]

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

for url in jobs:
    cursor.execute("""
    INSERT INTO jobs (url, company, status)
    VALUES (?, ?, ?)
    """, (url, "LinkedIn", "pending"))

conn.commit()

cursor.execute("SELECT * FROM jobs")
print(cursor.fetchall())

conn.close()