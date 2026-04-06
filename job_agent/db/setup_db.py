# setup_db.py
import sqlite3
import os

# Make sure 'db' folder exists
os.makedirs('db', exist_ok=True)

# Connect to SQLite database (file will be created automatically)
conn = sqlite3.connect('db/candidates.db')
c = conn.cursor()

# Create Users table
c.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    resume_path TEXT
)
''')

# Create CustomAnswers table
c.execute('''
CREATE TABLE IF NOT EXISTS CustomAnswers (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    field_name TEXT,
    answer TEXT
)
''')

# Create Jobs table
c.execute('''
CREATE TABLE IF NOT EXISTS Jobs (
    id INTEGER PRIMARY KEY,
    url TEXT,
    company TEXT,
    title TEXT,
    ats TEXT,
    status TEXT,
    fail_reason TEXT
)
''')

# Save (commit) changes and close
conn.commit()
conn.close()

print("✅ Database setup complete. File created at db/candidates.db")