# RPC Lab — Client–Server Implementation on AWS EC2

#### Alisher Berik, IT-2308, Astana IT University
#### Link to video: https://youtu.be/iAN6Dxl04yU
This project implements a minimal Remote Procedure Call (RPC) system using Python sockets and JSON.
The system includes a **server** that exposes remote functions and a **client** that sends RPC requests
with timeout and retry logic. The deployment runs on two separate AWS EC2 instances.

---

## 1. Project Structure

- `rpc_server.py` — RPC server (runs on EC2 server node)
- `rpc_client.py` — RPC client (runs on EC2 client node)

The RPC message format includes:

```json
{
  "request_id": "uuid",
  "method": "add",
  "params": {"a": 2, "b": 3}
}
```

The server returns:

```json
{
  "request_id": "uuid",
  "result": 5,
  "status": "OK"
}
```

---

## 2. AWS EC2 Setup (Two Nodes)

### Step 1 — Create Two Ubuntu Instances

1. Launch **Ubuntu 22.04** EC2 instances:
   - Instance 1: `rpc-client-node`
   - Instance 2: `rpc-server-node`

2. Create separate security groups or during creating the client node:

#### Server Security Group
Inbound:
- SSH (22) → My IP
- TCP 5000 → Source: `sg-xxxxxx` *(launch-wizard-1)* or `0.0.0.0/0` *(for testing)*


#### Client Security Group
Inbound:
- SSH (22) → My IP

Outbound:
- Allow all

---

## 3. Install Dependencies (Both Instances)

Run on both machines:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

---

## 4. Deploy RPC Server (Server Node)

Connect to the server:

```bash
ssh -i labsuser.pem ubuntu@<server-node-public-ip>
```

Create the file:

```bash
nano rpc_server.py
```

Paste server code, save, then run:

```bash
python3 rpc_server.py
```

The server will listen on port **5000**.

---

## 5. Deploy RPC Client (Client Node)

Connect to the client:

```bash
ssh -i labsuser.pem ubuntu@<client-node-public-ip>
```

Create client file:

```bash
nano rpc_client.py
```

Set `HOST = "<server-public-ip>"` inside the script.

Run:

```bash
python3 rpc_client.py
```

Expected output shows:
- results for successful RPC calls
- retry messages if timeout occurs

---

## 6. Connectivity Test (Optional)

From client machine:

```bash
nc -vz <server-public-ip> 5000
```

If successful, port 5000 is open.

---

## 7. Failure Handling Demonstration (Lab Requirement)

You may enable Artificial Delay scenario
On server.py, remove # commentary before this code on ~35 line:

```python
35      time.sleep(10)
```

Client triggers timeout → retries.


## 10. Credits

Alisher Berik, IT-2308, Astana IT University

