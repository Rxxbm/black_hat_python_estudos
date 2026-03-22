import socket 

target_host = "127.0.0.1" # No meu endereço IP local
target_port = 9998 # Porta acima de 1024 não requer root

# Criando um socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET é usado para declarar conexões IPv4
# DGRAM é usado para implementar o protocolo UDP

# Neste caso, o UDP não precisa de uma conexão como um TCP

client.sendto("Isso deve ser mostrado no servidor".encode(), (target_host, target_port))

# receber dados

data, addr = client.recvfrom(4096)

print(data)

print(addr)
