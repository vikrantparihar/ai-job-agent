import sqlite3

def get_next_job():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs WHERE status='pending' LIMIT 1")
    job = cursor.fetchone()

    conn.close()
    return job