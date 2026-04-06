import sqlite3

DB_PATH = "agent.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert user
    cursor.execute("""
    INSERT INTO users (name, email, skills, experience)
    VALUES (?, ?, ?, ?)
    """, (
        "Vikrant",
        "vikrant@example.com",
        "Python, AI, FastAPI",
        "Fresher"
    ))

    # Insert jobs
    jobs = [
        ("https://example.com/job1", "AI Engineer", "new"),
        ("https://example.com/job2", "ML Engineer", "new"),
        ("https://example.com/job3", "Backend Developer", "new")
    ]

    cursor.executemany("""
    INSERT INTO jobs (url, title, status)
    VALUES (?, ?, ?)
    """, jobs)

    conn.commit()
    conn.close()

    print("Seed Data Inserted 🚀")


if __name__ == "__main__":
    seed_data()