from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_conversion():
    if request.method == 'GET':
        return jsonify({
            "status": "Online",
            "active_version": "Push 2 Deployment",
            "instruction": "POST to / with {'celsius': val} OR {'fahrenheit': val}"
        })
        
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Missing JSON body."}), 400
            
        # Calculation Logic 1: Celsius to Fahrenheit
        if 'celsius' in data:
            try:
                c = float(data['celsius'])
                return jsonify({"celsius": c, "fahrenheit": (c * 9/5) + 32})
            except ValueError:
                return jsonify({"error": "Invalid numerical value."}), 400
                
        # Calculation Logic 2: Fahrenheit to Celsius
        elif 'fahrenheit' in data:
            try:
                f = float(data['fahrenheit'])
                return jsonify({"fahrenheit": f, "celsius": (f - 32) * 5/9})
            except ValueError:
                return jsonify({"error": "Invalid numerical value."}), 400
                
        else:
            return jsonify({"error": "Provide either 'celsius' or 'fahrenheit' values."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
