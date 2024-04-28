from flask import Flask, request, jsonify
from flask_cors import CORS
import data

app = Flask(__name__)
CORS(app)

city = {'Name': None, 'Data': None}

@app.route('/')
def foo():
    return jsonify({'HI': 'hi...'})

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    city['Name'] = query
    print(query)
    return jsonify({'result': query})

@app.route('/result')
def result():
    return jsonify({'City': city['Name']})

@app.route('/graph')
def graph():
    return data.generate_pie_chart(city['Name'])

if __name__ == '__main__':
    app.run(debug=True)