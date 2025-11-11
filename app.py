from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud system is live!"

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.get_json()
    print("Received from ESP32:", data)
    return jsonify({"status": "received", "message": "Data logged successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

