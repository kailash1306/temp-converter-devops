from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple JSON Home Page (No HTML)
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "Online",
        "service": "Temperature Converter API",
        "active_version": "Push 1 Deployment",
        "endpoints": {
            "POST /convert/c-to-f": "Expects json like {'celsius': 0}"
        }
    })

@app.route('/convert/c-to-f', methods=['POST'])
def c_to_f():
    data = request.get_json(silent=True)
    if not data or 'celsius' not in data:
        return jsonify({"error": "Missing 'celsius' value."}), 400
    try:
        c = float(data['celsius'])
        f = (c * 9/5) + 32
        return jsonify({"celsius": c, "fahrenheit": f})
    except ValueError:
        return jsonify({"error": "Invalid numerical value."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
