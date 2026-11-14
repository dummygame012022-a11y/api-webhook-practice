from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "order" not in data:
        return jsonify({"status": "error"}), 400
    with open("orders.csv", "a", newline="") as f:
        csv.writer(f).writerow([data["order"], data.get("item"), data.get("qty")])
    return jsonify({"status": "ok"})

app.run(host="127.0.0.1", port=8091)
