from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/state", methods=["GET"])
def getstatus():
    return jsonify({
        "isLive": True,
        "eventName": "test global object"
    })
