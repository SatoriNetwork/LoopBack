import socket
import sys

def check_port(ip, port, timeout=5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return True
        except socket.error:
            return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_port.py <ip> <port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Port must be an integer.")
        sys.exit(1)
    
    if check_port(ip, port):
        print(f"Port {port} on {ip} is open.")
    else:
        print(f"Port {port} on {ip} appears to be closed or filtered.")
