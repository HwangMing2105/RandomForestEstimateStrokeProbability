from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Khởi tạo Flask app
app = Flask(__name__)

# Load the trained model
rf_model = joblib.load('D:\Python\RandomForest\jupiter\stroke_prediction_model.pkl')

@app.route('/', methods=['GET'])
def home():
    return render_template('app.html')

# Định nghĩa route để dự đoán
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Lấy dữ liệu đầu vào từ người dùng
        data = request.json

        # Chuyển đổi dữ liệu đầu vào thành DataFrame và đảm bảo kiểu dữ liệu là số
        input_data = pd.DataFrame([data])
        input_data = input_data.astype(float)

        # Dự đoán tỷ lệ đột quỵ
        prediction = rf_model.predict(input_data)
        probability = rf_model.predict_proba(input_data)[:, 1]

        # Trả kết quả dự đoán
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': float(probability[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(port=6969, debug=True)