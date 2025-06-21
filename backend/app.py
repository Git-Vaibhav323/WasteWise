from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import io
from PIL import Image

app = Flask(__name__)
CORS(app) # Allow all origins

@app.route('/', methods=['GET'])
def index():
    return "Backend is running!"

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    
    try:
        # To simulate model processing, we'll just open the image
        # to ensure it's a valid image file.
        img = Image.open(file.stream)
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    # Simulate a classification result
    waste_types = ['plastic', 'paper', 'metal', 'organic', 'glass', 'cardboard']
    predicted_class = random.choice(waste_types)
    confidence = random.uniform(0.75, 0.99)

    # Placeholder disposal and recycling info
    disposal_method = f"This looks like {predicted_class}. Please dispose of it in the appropriate bin."
    recycling_centers = [
        {"name": "City Recycling Center", "address": "123 Green Way", "distance": "2.5 miles"},
        {"name": "Eco-friendly Disposal", "address": "456 Recycle Ave", "distance": "5 miles"}
    ]

    return jsonify({
        'type': predicted_class,
        'confidence': confidence,
        'disposal_method': disposal_method,
        'recycling_centers': recycling_centers
    })

if __name__ == '__main__':
    app.run(debug=True) 