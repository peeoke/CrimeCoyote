from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import data
import crimeIndex

app = Flask(__name__)
CORS(app)

city = {'Name': None, 'Ranking': None}

@app.route('/')
def foo():
    return jsonify({'HI': 'hi...'})

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    city['Name'] = query
    city['Ranking'] = crimeIndex.get_crime_rating(query)
    print(query)
    return jsonify({'result': query})

@app.route('/result')
def result():
    return jsonify({'City': city['Name'], 'Ranking': city['Ranking']})

@app.route('/graph')
def graph():
    data.generate_pie_chart(city['Name'])
    # Serve the image file
    return send_file('chart.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)