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
    <!doctype html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <style>
        body{{font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
              background:#f5f7fa;color:#222;margin:0;padding:40px;}}
        .card{{max-width:720px;margin:0 auto;background:#fff;padding:24px;border-radius:10px;
               box-shadow:0 8px 30px rgba(10,20,30,0.08);}}
        h2{{margin:0 0 12px;font-size:22px;color:#111;}}
        h4{{margin:6px 0;color:#444;font-weight:600;font-size:15px;}}
        .muted{{font-weight:400;color:#777;font-size:13px;margin-top:12px;}}
        @media (max-width:480px){{body{{padding:16px}}.card{{padding:16px}}}}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="muted"> Note: If you have deployed in K8s cluster please refresh page to see the changes below</div>
        <h4>Pod name: {pod_name}( to which pod the traffic is routed)</h4>
        <h4>Cluster IP: {server_ip}(cluster IP of that pod)</h4>
        <h4>Node IP: {client_ip}(on which node the pod is running)</h4>
        <div class="muted">Deployed with Flask in a Docker container</div>
      </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
