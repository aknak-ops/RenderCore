
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_script():
    data = request.json
    command = data.get("command")
    try:
        result = subprocess.run(["python"] + command.split(), capture_output=True, text=True)
        return jsonify({"output": result.stdout + result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
