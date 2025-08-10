
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/trigger", methods=["POST"])
def trigger_render():
    data = request.json
    batch = data.get("batch")
    if not batch:
        return jsonify({"error": "No batch name provided"}), 400
    try:
        result = subprocess.run(["python", "render_batch.py", batch], capture_output=True, text=True)
        return jsonify({"output": result.stdout + result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
