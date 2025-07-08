from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "🔍 Nmap Scan API is running!"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    target = data.get("target")

    if not target:
        return jsonify({
            "output": None,
            "error": "Missing 'target' in request body"
        }), 400

    try:
        # Run nmap with flags that do NOT require root
        result = subprocess.run(
            ["nmap", "-sT", "-Pn", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({
            "output": None,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    # For local testing only; avoid using this in production
    app.run(host="0.0.0.0", port=5000)
