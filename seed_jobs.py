import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

jobs = [
    ("https://www.linkedin.com/jobs/view/123456",),
    ("https://www.linkedin.com/jobs/view/654321",)
]

cursor.executemany("INSERT INTO jobs (url) VALUES (?)", jobs)

conn.commit()
conn.close()

print("✅ Jobs seeded")    
