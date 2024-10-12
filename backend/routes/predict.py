# routes/predict.py
from flask import Blueprint, request, jsonify
from backend.services.prediction_service import predict_species

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract required fields
        sepal_length = data['sepal_length']
        sepal_width = data['sepal_width']
        petal_length = data['petal_length']
        petal_width = data['petal_width']

        # Call the prediction service
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)

        # Return prediction result as JSON
        return jsonify({'species': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
