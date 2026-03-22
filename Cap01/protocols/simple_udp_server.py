import socket 

server_ip = "127.0.0.1"
server_port = 9998


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Usando endereço IPv4 no atributo AF_INET

# Usando server_ip e server_port para construir um servidor
server.bind((server_ip, server_port))

print(f"Ouvindo em {server_ip}:{server_port}")

while True:
    # Mostrando quem está se conectando no servidor
    data, addr =server.recvfrom(4096)
    print(f"Recebido: {data.decode()} de {addr}")
    print(f"Dados codificados: {data}")
    # Precisamos do addr para responder à solicitação ao cliente
    server.sendto(b"ACK!", addr)
    # É apenas uma convenção, mas precisa enviar em formato binário
