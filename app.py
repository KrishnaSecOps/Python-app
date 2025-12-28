import os
from kubernetes import client, config

def get_node_ip(node_name):
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    node = v1.read_node(node_name)
    for address in node.status.addresses:
        if address.type == "InternalIP":
            return address.address
    return "Unknown"

def main():
    pod_name = os.getenv("POD_NAME", "Unknown")
    node_name = os.getenv("NODE_NAME", "Unknown")

    node_ip = get_node_ip(node_name)

    print(f"Pod Name  : {pod_name}")
    print(f"Node Name : {node_name}")
    print(f"Node IP   : {node_ip}")

if __name__ == "__main__":
    main()
