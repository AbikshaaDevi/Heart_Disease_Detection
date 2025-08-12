from flask import Flask, render_template, request
import pickle
import numpy as np

# Load trained model & scaler
model = pickle.load(open("svm_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

# Feature order (8 features only)
features_list = ['age', 'sex', 'cp', 'thalach', 'exang', 'oldpeak', 'ca', 'thal']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form[feat]) for feat in features_list]
        data = np.array(data).reshape(1, -1)
        data = scaler.transform(data)
        prediction = model.predict(data)[0]

        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
