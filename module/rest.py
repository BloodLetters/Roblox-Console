from flask import Flask, request, jsonify
import logging
from datetime import datetime
import json
import os

CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

app = Flask(__name__)

@app.route('/script', methods=['GET'])
def handle_get():
    try:
        with open('script/source.lua', 'r', encoding='utf-8') as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return jsonify({"error": "File script/source.lua not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        message_type = data.get('type')
        message = data.get('message')
        
        if not message_type or not message:
            return jsonify({"error": "Missing 'type' or 'message' field"}), 400
        
        response = {
            "status": "success"
        }
        
        message_type_map = {
            "MessageOutput": ("\033[37m", "Info"),      # White
            "MessageInfo": ("\033[36m", "Info"),        # Cyan
            "MessageWarning": ("\033[33m", "Warning"),  # Yellow
            "MessageError": ("\033[31m", "Error")       # Red
        }
        
        current_time = datetime.now().strftime("%H:%M:%S")
        if message_type in message_type_map:
            color_code, type_name = message_type_map[message_type]
            print(f"{current_time} {color_code}{type_name}\033[0m: {color_code}{message}\033[0m")
        else:
            print(f"{current_time} \033[35mUnknown({message_type})\033[0m: \033[35m{message}\033[0m")
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def load_config():
    """Load configuration from config.json"""
    try:
        config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"port": 7243} 
    except Exception:
        return {"port": 7243}

def start_server(host='localhost', port=None, debug=False, use_ssl=True):
    """Function to start the HTTP/HTTPS server"""
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    if port is None:
        config = load_config()
        port = config.get('port', 7243)
    
    if use_ssl:
        app.run(host=host, port=port, ssl_context=(CERT_FILE, KEY_FILE), debug=debug)
    else:
        app.run(host=host, port=port, debug=debug)

@app.route('/script', methods=['GET'])
def handle_get_script():
    try:
        config = load_config()
        port = config.get('port', 7243)
        
        with open('script/source.lua', 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace('http://127.0.0.1:7243/console', f'http://127.0.0.1:{port}/api')
        
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return jsonify({"error": "File script/source.lua not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
