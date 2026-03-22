# Obtendo uma página do Google via cliente TCP
import socket

target_host = "www.google.com"
target_port = 80

# Criando um objeto socket simples
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET significa que usaremos um endereço IPv4 padrão
# SOCK_STREAM indica que o protocolo TCP será usado

# Conectando o cliente
client.connect((target_host, target_port))

# Enviando requisição HTTP - lembre-se que o HTTP é implementado pelo protocolo TCP
client.send("GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n".encode())
# Neste caso, estamos enviando o verbo HTTP GET para obter informações

# Recebendo dados do google.com
response = client.recv(4096)

# Exibindo a resposta recebida pela requisição HTTP
print(response)
