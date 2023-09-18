from flask import Flask, render_template, request, jsonify
from query import search

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html') #homepage

@app.route('/search', methods=['GET', 'POST'])
def search_route():
    query = request.json['query']
    return jsonify(search(query))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
