# import requests

# # Example for Gold API
# def get_gold_price():
#     url = 'https://api.gold-api.com/v1/latest'
#     params = {'apikey': 'goldapi-6kxg19lwiudgws-io'}
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data

# # Call the function
# gold_price = get_gold_price()
# print(f"Current gold price: {gold_price['price']} USD/oz")

# # Example for MetalpriceAPI
# def get_metalpriceapi_gold_price():
#     url = 'https://metalpriceapi.com/api/latest'
#     params = {'apikey': 'goldapi-6kxg19lwiudgws-io', 'base': 'USD', 'symbols': 'XAU'}
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data

# # Call the function
# gold_price = get_metalpriceapi_gold_price()
# print(f"Current gold price: {gold_price['rates']['XAU']} USD/oz")
# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# # Replace with your actual API details
# GOLD_API_URL = "https://api.goldapi.io/v1/latest"
# API_KEY = "your_api_key_here"

# def get_gold_price():
#     headers = {
#         'x-access-token': API_KEY
#     }
#     response = requests.get(GOLD_API_URL, headers=headers)
    
#     # Print the response for debugging
#     print(f"Status Code: {response.status_code}")
#     print(f"Response Text: {response.text}")

#     if response.status_code == 200:
#         try:
#             data = response.json()
#             return data
#         except requests.exceptions.JSONDecodeError as e:
#             print(f"JSON Decode Error: {e}")
#             return None
#     else:
#         print(f"Error: Unable to fetch data, status code {response.status_code}")
#         return None

# @app.route('/')
# def index():
#     return "Welcome to the Real-Time Gold Prices API"

# @app.route('/gold-price', methods=['GET'])
# def gold_price():
#     data = get_gold_price()
#     if data:
#         return jsonify(data)
#     else:
#         return jsonify({"error": "Unable to fetch gold prices"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API details
GOLD_API_URL = "https://www.goldapi.io/api/XAU/USD"
API_KEY = "goldapi-6kxg19lwiudgws-io"

def get_gold_price():
    headers = {
        'x-access-token': API_KEY
    }
    response = requests.get(GOLD_API_URL, headers=headers)
    
    # Print the response for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            return None
    else:
        print(f"Error: Unable to fetch data, status code {response.status_code}")
        return None

@app.route('/')
def index():
    return "Welcome to the Real-Time Gold Prices API"

@app.route('/gold-price', methods=['GET'])
def gold_price():
    data = get_gold_price()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch gold prices"}), 500

if __name__ == '__main__':
    app.run(debug=True)

pip freeze > requirements.txt




































