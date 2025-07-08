from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target = data.get('target')

    if not target:
        return jsonify({"error": "Target is required"}), 400

    try:
        # Run nmap scan for top 100 ports and OS detection
        result = subprocess.run(
            ['nmap', '-O', '--top-ports', '100', target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return jsonify({
            "output": result.stdout,
            "error": result.stderr
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Nmap Scan Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
