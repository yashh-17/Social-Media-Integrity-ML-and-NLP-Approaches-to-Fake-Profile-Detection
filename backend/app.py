from flask import Flask, request, jsonify, render_template
from model_utils import predict_account

app = Flask(__name__)

# Serve index.html at root URL
@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' is inside 'templates/' folder

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data from frontend
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Run prediction
    prediction = predict_account(data)
    
    # Return correct JSON response
    return jsonify({"result": prediction})

if __name__ == '__main__':
    app.run(debug=True)
