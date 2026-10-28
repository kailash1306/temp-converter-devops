from flask import Flask, request, jsonify

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    if not data or 'celsius' not in data:
        return jsonify({"error": "Please provide a 'celsius' value."}), 400
    
    try:
        c = float(data['celsius'])
        f = celsius_to_fahrenheit(c)
        return jsonify({
            "celsius": c,
            "fahrenheit": f
        })
    except ValueError:
        return jsonify({"error": "Invalid numerical value."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
