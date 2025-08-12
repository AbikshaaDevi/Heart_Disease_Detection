# Heart Disease Detection Using Flask & Machine Learning

A Flask web app that predicts the likelihood of heart disease using a trained machine learning model.

---

## Overview

This project processes a heart disease dataset, trains a classification model (e.g., Logistic Regression, Random Forest, Naive Bayes), and provides a web interface for users to input medical metrics and receive a prediction.

---

## Project Structure

```
Heart_Disease_Detection/
│
├── app.py
├── heart.csv (or relevant dataset file)
├── model.pkl
├── scaler.pkl (if using feature scaling)
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

---

## Setup & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbikshaaDevi/Heart_Disease_Detection.git
   cd Heart_Disease_Detection
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask app**
   ```bash
   python app.py
   ```
   Then open your browser and go to: `http://127.0.0.1:5000/`

4. **Make a prediction**  
   Fill in the required input fields (e.g., age, cholesterol, blood pressure, etc.) on the web form and submit to get a prediction.

---

## Deployment

You can deploy this application to platforms like Heroku, Render, or any hosting that supports Python & Flask.

---

## About the Author

This project was developed by **Abikshaa Devi** as a demonstration of integrating machine learning with web development to tackle real-world health prediction problems.

---

## Contributions

Feel free to:
- Improve model accuracy or try different algorithms (e.g., SVM, XGBoost)
- Add data validation and error handling
- Enhance UI/UX of the web interface
