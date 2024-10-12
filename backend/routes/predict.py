# routes/predict.py
from flask import Blueprint, request, jsonify, render_template
from backend.services.prediction_service import predict_species

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Call the prediction service
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)

        # Return prediction result as JSON
        return render_template('result.html', Predicted_flower_name=prediction)
        #return jsonify({'species': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
