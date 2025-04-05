from flask import Flask
import ssl

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure HTTPS Server!"

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  # Load SSL certs

    app.run(ssl_context=context, host="127.0.0.1", port=5000)
