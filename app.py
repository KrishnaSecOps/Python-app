from flask import Flask, request
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    # prefer downward API env var, fall back to hostname (K8s sets hostname to pod name by default)
    pod_name = os.environ.get("POD_NAME") or socket.gethostname()
    server_ip = socket.gethostbyname(socket.gethostname())
    client_ip = request.remote_addr

    return f"""
    <h1>Pod name: {pod_name}</h1>
    <h1>Cluster IP: {server_ip}</h1>
    <h1>Node IP: {client_ip}</h1>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
