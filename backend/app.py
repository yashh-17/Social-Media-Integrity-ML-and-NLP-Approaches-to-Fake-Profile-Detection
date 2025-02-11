from flask import Flask, request, jsonify, render_template
from model_utils import predict_account

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    if not data or "name" not in data:
        return jsonify({"error": "No valid data provided"}), 400

    name = data["name"]  # Extract name
    prediction = predict_account(data)  # Run the prediction

    return jsonify({"name": name, "result": prediction})  # Return name + prediction

if __name__ == '__main__':
    app.run(debug=True)
