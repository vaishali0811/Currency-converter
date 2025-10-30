# Currency Converter Backend
A Flask-based backend for a Dialogflow chatbot that converts currencies using real-time rates.

## Local Setup
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run: `python app.py`.

## Deployment
Deploy to Render via the dashboard, using `pip install -r requirements.txt` as build command and `python app.py` as start command.

## API Endpoint
POST to `/convert` with JSON: `{"from_currency": "USD", "to_currency": "EUR", "amount": 100}`.
