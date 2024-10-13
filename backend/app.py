# app.py
from flask import Flask, render_template
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from routes.predict import predict_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(predict_bp)

@app.route('/')
@app.route('/home')
def home():
#    return "Welcome to the Iris Classification API!"
    return render_template('home.html')

@app.route('/form')
def prediction():
    """
    docstring
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
