class RetryManager:

    MAX_RETRIES = 3

    def mark_processing(self, job):
        job.status = "processing"

    def mark_success(self, job):
        print("✅ JOB SUCCESS:", job.id)
        job.status = "completed"
        job.retry_count = 0

    def mark_failure(self, job, error):
        print("❌ JOB FAILED:", job.id, "ERROR:", error)

        if job.retry_count is None:
            job.retry_count = 0

        job.retry_count += 1

        if job.retry_count >= self.MAX_RETRIES:
            job.status = "failed"
        else:
            job.status = "pending"