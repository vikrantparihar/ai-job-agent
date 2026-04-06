import sqlite3

DB_PATH = "jobs.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
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

def add_job(title, description):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO jobs (title, description, status)
        VALUES (?, ?, 'pending')
    """, (title, description))

    conn.commit()
    conn.close()

def get_next_pending_job():
    conn = get_conn()
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
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        UPDATE jobs
        SET status=?
        WHERE id=?
    """, (status, job_id))

    conn.commit()
    conn.close()