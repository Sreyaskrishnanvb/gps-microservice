from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location')
def location():
    data = {
        "classroom": "IIIT Kottayam",
        "latitude": 10.0290,
        "longitude": 76.3264
    }
    return jsonify(data)

@app.route('/')
def home():
    return "GPS Microservice Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)