from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load dataset from JSON
with open('dataset/khodam.json', 'r', encoding='utf-8') as f:
    khodam_list = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    khodam = random.choice(khodam_list)
    result = {
        'name': name,
        'khodam_name': khodam['name'],
        'khodam_description': khodam['description']
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
