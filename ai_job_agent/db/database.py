# db/database.py

import sqlite3


# ✅ Connection function (IMPORTANT)
def get_conn():
    return sqlite3.connect("jobs.db")


# ✅ Init DB (tables create)
def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    # Jobs table (agent ke liye)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        status TEXT DEFAULT 'pending',
        failure_reason TEXT
    )
    """)

    # Applied jobs (tera old system)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applied_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# ✅ Save job (existing function)
def save_job(title, company, status):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO applied_jobs (title, company, status) VALUES (?, ?, ?)",
        (title, company, status)
    )

    conn.commit()
    conn.close()