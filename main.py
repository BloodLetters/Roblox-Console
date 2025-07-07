import sys
import os
import threading
import time

import module.rest as rest
import module.cert as cert
import module.conf as config

def cleaner():
    """Clear the console screen"""
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    """Print application banner"""
    print("=" * 50)
    print("    ROBLOX CONSOLE SERVER")
    print("=" * 50)

def startServer(port, use_ssl):
    """Start server in a separate thread"""
    try:
        rest.start_server(port=port, use_ssl=use_ssl)
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    cleaner()
    banner()
    
    print("Loading configuration...")
    config_data = config.read_config()
    use_ssl = config_data.get("method", "https") == "https"
    port = config_data.get("port", 7243)
    
    cert_file = 'cert.pem'
    key_file = 'key.pem'
    
    if use_ssl:
        print("Checking SSL certificates...")
        if not cert.check_ssl(cert_file, key_file):
            print("Generating SSL certificates...")
            cert.generateCert(cert_file, key_file)
        else:
            print("SSL certificates found.")

    config.create_source()
    server_thread = threading.Thread(target=startServer, args=(port, use_ssl))
    server_thread.daemon = True
    server_thread.start()
    time.sleep(2)
    
    cleaner()
    banner()
    protocol = "https" if use_ssl else "http"
    print(f"✓ Server running on {protocol}://localhost:{port}")
    print(f"✓ API endpoint: {protocol}://localhost:{port}/api")
    print(" ")
    print(f'✓ Script: loadstring(game:HttpGet("{protocol}://localhost:{port}/script", true))()')
    print("-" * 50)
    print("Server is running... Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")
        sys.exit(0)