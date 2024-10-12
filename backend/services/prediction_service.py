# services/prediction_service.py
import joblib
import numpy as np

# Load pre-trained model (this should be replaced with your actual path)
model = joblib.load('backend/model/iris_model.pkl')

def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    # Convert input into numpy array
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make prediction
    prediction = model.predict(input_features)

    # Map prediction to species name
    iris_species = {0: 'Setosa', 1: 'Versicolour', 2: 'Virginica'}
    return iris_species[prediction[0]]
