from flask import Flask, render_template, request, jsonify
import json
import os
import webbrowser
import threading

app = Flask(__name__)

CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"api_key": "", "model_provider": "", "model": ""}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

@app.route('/')
def index():
    config = load_config()
    return render_template('index.html', config=config)

@app.route('/save', methods=['POST'])
def save():
    config = request.json
    save_config(config)
    return jsonify({"status": "success"})

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

def run_config_ui():
    threading.Timer(1.25, open_browser).start()
    app.run(debug=False)