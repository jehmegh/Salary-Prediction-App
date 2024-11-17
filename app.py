import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
   
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Employee Salary should be $ {output}')
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

@app.route('/predict_api', methods=['POST'])
def predict_api():
    """
    For direct API calls through JSON data.
    """
    try:
        data = request.get_json(force=True)
        final_features = [np.array(list(data.values()))]
        prediction = model.predict(final_features)

        output = round(prediction[0], 2)
        return jsonify({'salary': output})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
