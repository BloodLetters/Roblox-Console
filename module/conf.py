import json
import os

def create_config():
    """Create config.json file with default settings"""
    config_data = {
        "method": "http",
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

def create_source():
    """Create source.lua file by fetching content from GitHub"""
    import urllib.request
    
    url = "https://raw.githubusercontent.com/BloodLetters/Roblox-Console/refs/heads/main/script/source.lua"
    source_path = "script/source.lua"
    
    try:
        with urllib.request.urlopen(url) as response:
            source_content = response.read().decode('utf-8')

        os.makedirs(os.path.dirname(source_path), exist_ok=True)
        with open(source_path, 'w', encoding='utf-8') as source_file:
            source_file.write(source_content)
        
        print(f"Source file created at: {os.path.abspath(source_path)}")
        
    except Exception as e:
        print(f"Error fetching source file: {e}")
        source_content = "-- Roblox Console Script\nprint('This is an error message. please open issue on github!')"
        os.makedirs(os.path.dirname(source_path), exist_ok=True)
        with open(source_path, 'w') as source_file:
            source_file.write(source_content)
        print(f"Fallback source file created at: {os.path.abspath(source_path)}")