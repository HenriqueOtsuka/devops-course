from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/appstatus', methods=['GET'])
def app_status():
    return jsonify({'status': True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
