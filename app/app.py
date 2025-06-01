from flask import Flask, request, jsonify, send_from_directory
import redis
import os

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/write", methods=["POST"])
def write():
    data = request.json.get("data")
    r.set("key", data)
    return jsonify({"status": "success", "written": data})

@app.route("/read", methods=["GET"])
def read():
    data = r.get("key")
    return jsonify({"data": data})

@app.route("/")
def index():
    return send_from_directory(os.path.join(app.root_path, "static"), "test.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
