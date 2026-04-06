import json
import time
from datetime import datetime, timedelta

BACKLOG_FILE = "backlog.json"


# 🔹 Load backlog
def load_data():
    try:
        with open(BACKLOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


# 🔹 Save backlog
def save_data(data):
    with open(BACKLOG_FILE, "w") as f:
        json.dump(data, f, indent=4)


# 🔹 Add job (run once)
def add_job(url):
    data = load_data()

    job = {
        "url": url,
        "status": "failed",
        "retry_count": 0,
        "next_retry": str(datetime.now())
    }

    data.append(job)
    save_data(data)

    print("✅ Job added:", url)


# 🔹 Smart delay (Exponential Backoff)
def get_next_retry(retry_count):
    if retry_count == 1:
        return datetime.now() + timedelta(seconds=10)
    elif retry_count == 2:
        return datetime.now() + timedelta(seconds=30)
    else:
        return datetime.now() + timedelta(seconds=60)


# 🔹 Fake apply function (later replace with real)
def apply_job(url):
    print("Applying to:", url)

    # ❌ demo fail (change later)
    return False


# 🔹 Retry system
def retry_jobs():
    data = load_data()

    for job in data:

        # skip completed jobs
        if job.get("status") in ["success", "permanent_failed"]:
            continue

        # default values (safety)
        job.setdefault("retry_count", 0)
        job.setdefault("next_retry", str(datetime.now()))

        # ⏱️ check retry time
        next_time = datetime.fromisoformat(job["next_retry"])
        if datetime.now() < next_time:
            continue

        print("\n🔍 Checking:", job["url"])

        success = apply_job(job["url"])

        if success:
            job["status"] = "success"
            print("✅ Success")

        else:
            job["retry_count"] += 1
            print(f"❌ Attempt {job['retry_count']} failed")

            if job["retry_count"] >= 3:
                job["status"] = "permanent_failed"
                print("🚫 Permanent Fail")

            else:
                job["status"] = "retrying"
                next_time = get_next_retry(job["retry_count"])
                job["next_retry"] = str(next_time)

                print("🔁 Next retry at:", next_time)

    save_data(data)


# 🔹 MAIN LOOP
if __name__ == "__main__":
    # 👉 run only first time (comment later)
    add_job("https://example.com")

    while True:
        retry_jobs()
        time.sleep(5)

