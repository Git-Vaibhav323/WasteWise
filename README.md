# WasteWise 🌱

An AI-powered web platform for smart waste management and recycling.

## Features

- 🖼️ AI-powered waste type detection from images
- ♻️ Smart disposal and recycling recommendations
- 📍 Local recycling center locator
- 🎮 Gamified eco-actions for sustainable behavior

## Tech Stack

- **Frontend**: React + Tailwind CSS
- **Backend**: Flask + Python
- **AI/ML**: TensorFlow/PyTorch with pre-trained models
- **Maps**: Google Maps API

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask server:
```bash
python backend/app.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

## Environment Variables

Create a `.env` file in the backend directory with:
```
GOOGLE_MAPS_API_KEY=your_api_key_here
```

## Contributing

Feel free to submit issues and enhancement requests! 