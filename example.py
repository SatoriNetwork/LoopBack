# curl -X POST -H "Content-Type: application/json" -d '{"ip": "203.0.113.45", "port": 8080}' http://<your_server>:5000/check

import requests

url = "http://your_remote_server:5000/check"  # Replace with your remote server's address and port
payload = {
    "ip": "203.0.113.45",  # Target public IP
    "port": 8080         # Target port to test
}

response = requests.post(url, json=payload)
if response.status_code == 200:
    result = response.json()
    print("Response from server:", result)
else:
    print("Error:", response.status_code, response.text)
