import asyncio
from flask import Flask, request, jsonify
import websockets

app = Flask(__name__)

async def check_websocket(ip, port, timeout=5):
    uri = f"ws://{ip}:{port}/"
    try:
        async with websockets.connect(uri, timeout=timeout):
            # handshake succeeded
            return True
    except Exception:
        return False

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    if not data or "ip" not in data or "port" not in data:
        return jsonify({"error": "Missing 'ip' or 'port' in request"}), 400

    ip = data["ip"]
    try:
        port = int(data["port"])
    except ValueError:
        return jsonify({"error": "'port' must be an integer"}), 400

    # Run the asynchronous WebSocket check in a new event loop.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(check_websocket(ip, port))
    loop.close()

    return jsonify({"ip": ip, "port": port, "websocket_open": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
