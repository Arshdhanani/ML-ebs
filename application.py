from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from PIL import Image
import numpy as np
import cv2
import io
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError

application = Flask(__name__)
CORS(application)  # Enable CORS for all routes

# Define custom objects
custom_objects = {
    'mse': MeanSquaredError()
}

# Load your model with custom objects
model = load_model(r'ML-ebs\trained_model.h5', custom_objects=custom_objects)

@application.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    try:
        image = Image.open(image_file.stream)
    except IOError:
        return jsonify({'error': 'Invalid image format'}), 400

    # Preprocess the image for the model
    new_image = image.resize((224, 224))
    new_image_array = np.array(new_image) / 255.0
    new_image_array = np.expand_dims(new_image_array, axis=0)

    # Predict using the model
    prediction = model.predict(new_image_array)

    # Process the prediction to generate the output image
    predicted_points = prediction[0].reshape(-1, 2).astype(int)
    resized_image = cv2.resize(np.array(image), (224, 224))
    cv2.polylines(resized_image, [predicted_points], isClosed=True, color=(0, 255, 0), thickness=1)

    # Convert the processed image to bytes
    is_success, buffer = cv2.imencode(".png", resized_image)
    if not is_success:
        return jsonify({'error': 'Failed to encode image'}), 500
    
    io_buf = io.BytesIO(buffer)

    return send_file(io_buf, mimetype='image/png')

@application.route('/')
def index():
    return send_from_directory('templates', 'index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
