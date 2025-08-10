from backend.history_logger import log_history
from datetime import datetime

log_history({
    "id": "999",
    "prompt": "Manual test log",
    "status": "completed",
    "start_time": datetime.now().isoformat(),
    "end_time": datetime.now().isoformat(),
    "duration": "0:00:01",
    "output": "output/test/999_output.txt"
})
