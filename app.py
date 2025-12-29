from flask import Flask, request
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    client_ip = request.remote_addr

    return f"""
    <h1>Server IP: {server_ip}</h1>
    <h1>Client IP: {client_ip}</h1>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
