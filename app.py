from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

QURAN_API_URL = "https://quran-api.santrikoding.com/api/surah"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/surah')
def get_surah():
    response = requests.get(QURAN_API_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
