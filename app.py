from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        return rates.get(to_currency.upper(), None)
    return None

@app.route('/convert', methods=['POST'])
def convert_currency():
    try:
        data = request.get_json()
        from_currency = data.get('from_currency', '').upper()
        to_currency = data.get('to_currency', '').upper()
        amount = float(data.get('amount', 0))
        
        if not from_currency or not to_currency or amount <= 0:
            return jsonify({"error": "Invalid input. Provide from_currency, to_currency, and a positive amount."}), 400
        
        rate = get_exchange_rate(from_currency, to_currency)
        if rate is None:
            return jsonify({"error": f"Unable to fetch rate for {from_currency} to {to_currency}."}), 500
        
        converted_amount = amount * rate
        return jsonify({
            "converted_amount": round(converted_amount, 2),
            "rate": rate,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "original_amount": amount
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Currency Converter Backend is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
