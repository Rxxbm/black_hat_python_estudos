import socket

target_ip = "127.0.0.1"
target_port = 9999

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect((target_ip, target_port))

bytes_sent = socket_client.send(b"Sending a protected file to server")

data = socket_client.recv(4096)

print(f"Received: {data.decode()}")
