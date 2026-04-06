import sqlite3

DB_NAME = "job_agent.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT DEFAULT 'pending'
    )
    """)

    conn.commit()
    conn.close()


# ✅ ADD THIS (IMPORTANT)
def insert_job(title, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO jobs (title, description, status) VALUES (?, ?, ?)",
        (title, description, "pending")
    )

    conn.commit()
    conn.close()


# Worker ke liye
def get_next_job():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, description FROM jobs WHERE status='pending' LIMIT 1"
    )

    job = cursor.fetchone()
    conn.close()

    return job


def update_job_status(job_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jobs SET status=? WHERE id=?",
        (status, job_id)
    )

    conn.commit()
    conn.close()
