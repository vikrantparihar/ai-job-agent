from db.database import get_conn


class Job:
    def __init__(self, id, url):
        self.id = id
        self.url = url


def get_next_job():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT id, url FROM jobs WHERE status='pending' LIMIT 1")
    row = cursor.fetchone()

    conn.close()

    if row:
        return Job(row[0], row[1])
    return None


def update_job_status(job_id, status):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jobs SET status=? WHERE id=?",
        (status, job_id)
    )

    conn.commit()
    conn.close()