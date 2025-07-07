import json
import os

def create_config():
    """Create config.json file with default settings"""
    config_data = {
        "method": "https",
        "port": 7243,
        "logSave": False
    }
    
    config_path = "config.json"

    with open(config_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)
    
    print(f"Config file created at: {os.path.abspath(config_path)}")

def read_config():
    """Read config.json file and return the configuration data"""
    config_path = "config.json"
    
    if not os.path.exists(config_path):
        create_config()
    
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def set_config(config_json):
    """Update config.json file with new configuration data"""
    config_path = "config.json"
    
    with open(config_path, 'w') as config_file:
        json.dump(config_json, config_file, indent=4)
    
    print(f"Config file updated at: {os.path.abspath(config_path)}")
