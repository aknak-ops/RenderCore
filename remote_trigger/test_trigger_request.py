
import requests

payload = {
    "batch": "test_batch"
}

res = requests.post("http://localhost:8000/trigger", json=payload)
print(res.status_code)
print(res.json())
