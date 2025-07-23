from flask import Flask, render_template, jsonify
import os, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summary")
def summary():
    try:
        with open("output/test/summary.json") as f:
            data = json.load(f)
        return jsonify(data)
    except:
        return jsonify({"error": "summary.json not found"})

if __name__ == "__main__":
    app.run(debug=True)