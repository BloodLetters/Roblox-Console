import os
from OpenSSL import crypto

def generateCert(cert_file, key_file):
    if os.path.exists(cert_file) and os.path.exists(key_file):
        print(f"SSL certificates already exist: {cert_file}, {key_file}")
        return True

    print("Generating self-signed SSL certificate...")
    
    try:
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 2048)

        cert = crypto.X509()
        cert.get_subject().CN = "localhost"
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        with open(cert_file, "wt") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
        with open(key_file, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))
        
        print(f"SSL certificate generated: {cert_file}, {key_file}")
        return True
        
    except Exception as e:
        print(f"Error generating SSL certificate: {e}")
        return False

def check_ssl(cert_file, key_file):
    if os.path.exists(cert_file) and os.path.exists(key_file):
        return True
    else:
        return False
