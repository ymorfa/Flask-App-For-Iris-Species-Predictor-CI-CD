# app.py
from flask import Flask
from backend.routes.predict import predict_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return "Welcome to the Iris Classification API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
