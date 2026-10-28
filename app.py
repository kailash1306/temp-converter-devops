from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/', methods=['GET'])
def home():
    return "welcome to homepage"

@app.route('/convert/c-to-f', methods=['POST'])
def c_to_f():
    data = request.get_json(silent=True)
    if not data or 'celsius' not in data:
        return jsonify({"error": "Missing 'celsius' value."}), 400
    try:
        c = float(data['celsius'])
        return jsonify({"celsius": c, "fahrenheit": celsius_to_fahrenheit(c)})
    except ValueError:
        return jsonify({"error": "Invalid numerical value."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
