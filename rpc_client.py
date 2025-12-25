import socket
import json
import uuid

HOST = "<server-public-ip>"
PORT = 5000
TIMEOUT = 2  # seconds
MAX_RETRIES = 3

def rpc_call(method, params):
    request_id = str(uuid.uuid4())
    request = {
        "request_id": request_id,
        "method": method,
        "params": params
    }
    
    for attempt in range(MAX_RETRIES):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(TIMEOUT)
                s.connect((HOST, PORT))
                s.sendall(json.dumps(request).encode())
                data = s.recv(1024)
                response = json.loads(data.decode())
                if response.get("status") == "OK":
                    print("Result:", response.get("result"))
                else:
                    print("Error:", response.get("status"))
                return
        except socket.timeout:
            print(f"Timeout, retrying {attempt+1}/{MAX_RETRIES}...")
        except Exception as e:
            print("Error:", e)
    print("RPC failed after retries.")

# Example calls
rpc_call("add", {"a": 5, "b": 7})
rpc_call("reverse_string", {"s": "hello"})
