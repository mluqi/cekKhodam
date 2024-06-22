from flask import Flask, jsonify, request, render_template, url_for
import json
import random

app = Flask(__name__)

# Load khodam data from JSON file
with open('khodam.json') as f:
    khodam_data = json.load(f)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    
    # Select random khodam
    selected_khodam = random.choice(khodam_data)
    
    result = {
        'name': name,
        'khodam_name': selected_khodam['name'],
        'khodam_description': selected_khodam['description']
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
