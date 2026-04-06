import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('db/candidates.db')
c = conn.cursor()

# Insert a demo user
c.execute('''
INSERT INTO Users (name, email, phone, resume_path)
VALUES (?, ?, ?, ?)
''', ("John Doe", "john@example.com", "9999999999", "resumes/john_resume.pdf"))

conn.commit()
conn.close()

print("✅ Demo user added to the database!")
