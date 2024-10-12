# ABIChallenge_YamilMorfa
AB InBev MLOps Challenge Yamil Ernesto Morfa

## Overview
This project implements a simple Flask API to classify Iris species using a pre-trained machine learning model. The API predicts the species based on the input features provided, such as sepal length, sepal width, petal length, and petal width.

## Steps to Develop the Project

### 1. Model Creation
The initial step involved creating a Jupyter Notebook to train and test the machine learning model.

- Notebook: `notebooks/IrisClassification.ipynb`
- In this notebook, I loaded the Iris dataset, trained a model, and evaluated its performance.
- After ensuring the model was working correctly, I saved it as `iris_model.pkl` to be used in the backend API.

### 2. Backend API Development
Next, I created a Flask application to serve the predictions through an API.

The main application file is located at `backend/app.py`.
I created an API endpoint `/predict` to accept POST requests with the required input features in JSON format and return the predicted species.

### 3. Unit Testing
I implemented unit tests to verify that the API behaves as expected. The test file is located at tests/test_app.py.
I created tests for both successful predictions and invalid input handling.

### File Structure
```bash
root
├── backend/
│   ├── app.py                # Main Flask app
│   ├── requirements.txt      # Dependencies requirements
│   ├── model/
│   │   └── iris_model.pkl    # Pre-trained model
│   ├── routes/
│   │   └── predict.py        # Prediction route handler
│   └── services/
│       └── prediction_service.py # Business logic
│ 
├── notebooks
│   └── IrisClassification.ipynb # model experimentations
├── tests
│   └── test_app.py # Unit Testing to verify that the API behaves as expected

```

# Step by step guide to run

1. Clone this repo

## Install requirements

```bash
pip install -r requirements.txt
```