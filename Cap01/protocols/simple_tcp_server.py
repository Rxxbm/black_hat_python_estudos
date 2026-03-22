import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print(f"Ouvindo em {bind_ip}:{bind_port}")

def handleClient(client_socket):
    request = client_socket.recv(4096)

    print(f"Recebido {request}")

    client_socket.send(b"ACK!")
    client_socket.close()

while True:
    # Isso cria uma linha privada de telefone com o host
    client, addr = server.accept()
    print(f"Conexão aceita de {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handleClient,args=(client,))
    client_handler.start()
