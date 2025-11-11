from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Women Safety IoT Cloud System is Running!"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("Alert Received:", data)
    return jsonify({"message": "Alert Received Successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
