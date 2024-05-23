from flask import Flask, jsonify
import requests
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Fetch the service account key JSON file contents
cred = credentials.Certificate("path/to/your-firebase-adminsdk.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred)

db = firestore.client()

GOLD_API_URL = "https://www.goldapi.io/api/XAU/USD"
HEADERS = {'x-access-token': 'goldapi-6kxg19lwiudgws-io'}

@app.route('/gold_price', methods=['GET'])
def get_gold_price():
    response = requests.get(GOLD_API_URL, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        # Save the fetched gold price to Firebase
        db.collection('gold_prices').add(data)
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch gold price'}), response.status_code

@app.route('/gold_prices', methods=['GET'])
def get_gold_prices():
    gold_prices_ref = db.collection('gold_prices')
    docs = gold_prices_ref.stream()
    prices = [doc.to_dict() for doc in docs]
    return jsonify(prices)

if __name__ == '__main__':
    app.run()
