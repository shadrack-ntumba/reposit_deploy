from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
timer_duration = 0

# Configuration de l'emplacement du dossier des fichiers HTML
base_dir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return send_from_directory(base_dir, 'input_time.html')

@app.route('/timer.html')
def timer():
    return send_from_directory(base_dir, 'timer.html')

@app.route('/set_timer', methods=['POST'])
def set_timer():
    global timer_duration
    data = request.get_json()
    timer_duration = int(data['time'])
    return jsonify(success=True)

@app.route('/get_timer', methods=['GET'])
def get_timer():
    global timer_duration
    return jsonify(time=timer_duration)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
