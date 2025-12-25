import socket
import json
import time

def add(a, b):
    return a + b

def reverse_string(s):
    return s[::-1]

# Map function names to actual functions
FUNCTIONS = {
    "add": add,
    "reverse_string": reverse_string
}

HOST = '0.0.0.0'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            if not data:
                continue
            request = json.loads(data.decode())
            func_name = request.get("method")
            params = request.get("params", {})
            
            # time.sleep(10)  # failure scenario

            if func_name in FUNCTIONS:
                result = FUNCTIONS[func_name](**params)
                response = {
                    "request_id": request["request_id"],
                    "result": result,
                    "status": "OK"
                }
            else:
                response = {
                    "request_id": request["request_id"],
                    "result": None,
                    "status": "ERROR: Unknown method"
                }
            conn.sendall(json.dumps(response).encode())
