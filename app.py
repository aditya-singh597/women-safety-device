from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloud system is live!"

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "OK", "message": "Data received successfully"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render assigns this automatically
    app.run(host='0.0.0.0', port=port)


