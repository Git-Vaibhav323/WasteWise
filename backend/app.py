from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Define a translation dictionary for Vietnamese waste labels
WASTE_LABEL_TRANSLATIONS = {
    "plastic nhựa": "Plastic",
    "giấy": "Paper",
    "kim loại": "Metal",
    "thủy tinh": "Glass",
    "hữu cơ": "Organic",
    "vải": "Fabric",
    "điện tử": "Electronic",
    "khác": "Other"
}

# Define example dynamic responses based on waste types
DYNAMIC_RESPONSES = {
    "Plastic": {
        "disposal_method": "Recycle in plastic bin. Ensure it's clean and dry.",
        "recycling_centers": [
            {'name': 'City Plastic Recycling', 'address': '456 Industrial Rd', 'distance': '5.0 km'}
        ]
    },
    "Paper": {
        "disposal_method": "Recycle in paper/cardboard bin. Keep dry.",
        "recycling_centers": [
            {'name': 'Community Paper Collection', 'address': '789 Main St', 'distance': '1.2 km'}
        ]
    },
    "Metal": {
        "disposal_method": "Recycle in metal/can bin. Empty and rinse if applicable.",
        "recycling_centers": [
            {'name': 'Metal Scraps Inc.', 'address': '101 Steel Ave', 'distance': '7.8 km'}
        ]
    },
    "Glass": {
        "disposal_method": "Recycle in glass bin. No broken glass please.",
        "recycling_centers": [
            {'name': 'Glass Recycling Depot', 'address': '202 Bottle Rd', 'distance': '3.1 km'}
        ]
    },
    "Organic": {
        "disposal_method": "Compost at home or use organic waste collection.",
        "recycling_centers": [
            {'name': 'Local Composting Site', 'address': '303 Garden Ln', 'distance': '0.8 km'}
        ]
    },
    "Fabric": {
        "disposal_method": "Donate to charity or textile recycling. Not for general waste.",
        "recycling_centers": [
            {'name': 'Textile Donation Center', 'address': '404 Cloth St', 'distance': '4.5 km'}
        ]
    },
    "Electronic": {
        "disposal_method": "Take to special e-waste collection points. Do not dispose of with regular trash.",
        "recycling_centers": [
            {'name': 'E-Waste Disposal Hub', 'address': '505 Circuit Blvd', 'distance': '6.2 km'}
        ]
    },
    "Other": {
        "disposal_method": "Check local guidelines for proper disposal of mixed waste.",
        "recycling_centers": [
            {'name': 'General Waste Facility', 'address': '606 Dump Rd', 'distance': '9.0 km'}
        ]
    }
}

# Initialize the model (we'll load a pre-trained model later)
model = None

def load_model():
    global model
    # TODO: Load pre-trained model
    pass

def preprocess_image(image):
    # TODO: Implement image preprocessing
    pass

@app.route('/api/classify', methods=['POST'])
def classify_waste():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        image = request.files['image']
        # TODO: Here, the actual ML model would classify the image
        # For now, we'll simulate a random classification
        
        # Pick a random English waste type
        random_english_label = random.choice(list(DYNAMIC_RESPONSES.keys()))
        
        # Get corresponding dynamic response details
        response_details = DYNAMIC_RESPONSES.get(random_english_label, DYNAMIC_RESPONSES["Other"])

        return jsonify({
            'type': random_english_label,
            'confidence': round(random.uniform(0.70, 0.99), 2),
            'disposal_method': response_details["disposal_method"],
            'recycling_centers': response_details["recycling_centers"]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recycling-centers', methods=['GET'])
def get_recycling_centers():
    # TODO: Implement Google Maps API integration
    return jsonify({
        'centers': [
            {
                'name': 'Local Recycling Center',
                'address': '123 Green St',
                'distance': '2.5 km',
                'coordinates': {'lat': 0, 'lng': 0}
            }
        ]
    })

if __name__ == '__main__':
    load_model()
    app.run(debug=True) 