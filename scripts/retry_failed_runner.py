from core.backend.retry_failed import retry_failed_jobs

count = retry_failed_jobs("core/queue.csv")
print(f"[✓] Reset {count} failed job(s) to pending.")
