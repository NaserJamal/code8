# from flask import Flask, render_template, request, jsonify
# import json
# import os
# import webbrowser
# import threading
# from .test_generator import generate_tests

# app = Flask(__name__)

# CONFIG_FILE = 'config.json'

# def load_config():
#     if os.path.exists(CONFIG_FILE):
#         with open(CONFIG_FILE, 'r') as f:
#             return json.load(f)
#     return {"api_key": "", "model_provider": "", "model": ""}

# def save_config(config):
#     with open(CONFIG_FILE, 'w') as f:
#         json.dump(config, f)

# @app.route('/')
# def index():
#     config = load_config()
#     return render_template('index.html', config=config)

# @app.route('/save', methods=['POST'])
# def save():
#     config = request.json
#     save_config(config)
#     return jsonify({"status": "success"})

# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:5000/')

# def run_config_ui():
#     threading.Timer(1.25, open_browser).start()
#     app.run(debug=False)
# import os
# import json
# import asyncio
# import webbrowser
# from flask import Flask, render_template, request, jsonify
# from .test_generator import generate_tests

# app = Flask(__name__)

# CONFIG_FILE = 'config.json'

# def load_config():
#     if os.path.exists(CONFIG_FILE):
#         with open(CONFIG_FILE, 'r') as f:
#             return json.load(f)
#     return {"api_key": "", "model_provider": "", "model": ""}

# def save_config(config):
#     with open(CONFIG_FILE, 'w') as f:
#         json.dump(config, f)

# @app.route('/')
# def index():
#     config = load_config()
#     return render_template('index.html', config=config)

# @app.route('/save', methods=['POST'])
# def save():
#     config = request.json
#     save_config(config)
#     return jsonify({"status": "success"})

# @app.route('/browse')
# def browse():
#     path = request.args.get('path', '.')
#     items = []
#     for item in os.listdir(path):
#         full_path = os.path.join(path, item)
#         items.append({
#             'name': item,
#             'path': full_path,
#             'type': 'directory' if os.path.isdir(full_path) else 'file'
#         })
#     return jsonify(items)

# @app.route('/run_tests', methods=['POST'])
# def run_tests():
#     files = request.json['files']
    
#     async def run_tests_async():
#         tasks = [asyncio.to_thread(generate_tests, file) for file in files]
#         await asyncio.gather(*tasks)
    
#     asyncio.run(run_tests_async())
#     return jsonify({"status": "success", "message": f"Tests generated for {len(files)} files"})

# def run_config_ui():
#     webbrowser.open('http://127.0.0.1:5000/')
#     app.run(debug=False)

# if __name__ == '__main__':
#     run_config_ui()
# import os
# import json
# import asyncio
# import webbrowser
# from flask import Flask, render_template, request, jsonify
# from .test_generator import generate_tests

# app = Flask(__name__)

# CONFIG_FILE = 'config.json'

# def load_config():
#     if os.path.exists(CONFIG_FILE):
#         with open(CONFIG_FILE, 'r') as f:
#             return json.load(f)
#     return {
#         "api_key": "", 
#         "model_provider": "", 
#         "model": "",
#         "system_prompt": "You are a helpful assistant that generates Python unit tests for the file named '{file_name}'. Do not include code blocks or explanations in your response, just the unittest code.",
#         "user_prompt": "Please generate unit tests for the following Python code from the file '{file_name}':\n\n{code_content}\n\nProvide a complete unittest class with test methods for each function in the code.\nDo not include any explanations or code blocks, just the unittest code."
#     }

# def save_config(config):
#     with open(CONFIG_FILE, 'w') as f:
#         json.dump(config, f)

# @app.route('/')
# def index():
#     config = load_config()
#     return render_template('index.html', config=config)

# @app.route('/save', methods=['POST'])
# def save():
#     config = request.json
#     save_config(config)
#     return jsonify({"status": "success"})

# @app.route('/browse')
# def browse():
#     path = request.args.get('path', '.')
#     items = []
#     for item in os.listdir(path):
#         full_path = os.path.join(path, item)
#         items.append({
#             'name': item,
#             'path': full_path,
#             'type': 'directory' if os.path.isdir(full_path) else 'file'
#         })
#     return jsonify(items)

# @app.route('/run_tests', methods=['POST'])
# def run_tests():
#     files = request.json['files']
#     config = load_config()
    
#     async def run_tests_async():
#         tasks = [asyncio.to_thread(generate_tests, file, config['system_prompt'], config['user_prompt']) for file in files]
#         await asyncio.gather(*tasks)
    
#     asyncio.run(run_tests_async())
#     return jsonify({"status": "success", "message": f"Tests generated for {len(files)} files"})

# def run_config_ui():
#     webbrowser.open('http://127.0.0.1:5000/')
#     app.run(debug=False)

# if __name__ == '__main__':
#     run_config_ui()
import os
import json
import asyncio
import webbrowser
from flask import Flask, render_template, request, jsonify
from .test_generator import generate_tests, load_config

app = Flask(__name__)

CONFIG_FILE = 'config.json'

@app.route('/')
def index():
    config = load_config()
    return render_template('index.html', config=config)

@app.route('/save', methods=['POST'])
def save():
    config = request.json
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    return jsonify({"status": "success"})

@app.route('/browse')
def browse():
    path = request.args.get('path', '.')
    items = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        items.append({
            'name': item,
            'path': full_path,
            'type': 'directory' if os.path.isdir(full_path) else 'file'
        })
    return jsonify(items)

@app.route('/run_tests', methods=['POST'])
def run_tests():
    files = request.json['files']
    config = load_config()
    
    async def run_tests_async():
        tasks = [asyncio.to_thread(generate_tests, file, config['system_prompt'], config['user_prompt']) for file in files]
        await asyncio.gather(*tasks)
    
    asyncio.run(run_tests_async())
    return jsonify({"status": "success", "message": f"Tests generated for {len(files)} files"})

def run_config_ui():
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)

if __name__ == '__main__':
    run_config_ui()