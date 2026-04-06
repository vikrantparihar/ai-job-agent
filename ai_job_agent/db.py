import sqlite3

DB_NAME = "jobs.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)

    conn.commit()
    conn.close()
    print("DB Ready")

def add_job(title, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO jobs (title, description, status)
        VALUES (?, ?, 'pending')
    """, (title, description))

    conn.commit()
    conn.close()

def get_next_job():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, title, description
        FROM jobs
        WHERE status='pending'
        ORDER BY id ASC
        LIMIT 1
    """)

    job = cur.fetchone()
    conn.close()
    return job

def update_job_status(job_id, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE jobs
        SET status=?
        WHERE id=?
    """, (status, job_id))

    conn.commit()
    conn.close()