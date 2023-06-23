from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    data = {
        'name': 'Your Startup Company',
        'description': 'Welcome to our API!',
        'version': '1.0'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
