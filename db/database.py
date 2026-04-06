import sqlite3

def get_conn():
    return sqlite3.connect("jobs.db")


def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY,
        url TEXT,
        company TEXT,
        status TEXT,
        ats TEXT,
        failure_reason TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()