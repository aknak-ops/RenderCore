import csv

def retry_failed_jobs(queue_file):
    updated = 0
    with open(queue_file, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        if row.get("status", "").strip().lower() == "failed":
            row["status"] = "pending"
            updated += 1

    with open(queue_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "prompt", "status"])
        writer.writeheader()
        writer.writerows(rows)

    return updated
