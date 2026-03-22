import socket
import threading
import sys

def server_loop(local_host: str, local_port: int, remote_host: str, remote_port: int, receive_first: bool):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reiniciar o proxy rápido
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print(f"[!!] Falha ao iniciar servidor em {local_host}:{local_port}")
        print(f"[!!] Erro: {e}")
        sys.exit(0)

    print(f"[*] Escutando em {local_host}:{local_port}")
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print(f"[>] Conexão recebida de {addr[0]}:{addr[1]}")
        proxy_thread = threading.Thread(
            target=proxy_handler, 
            args=(client_socket, remote_host, remote_port, receive_first)
        )
        proxy_thread.start()

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        remote_socket.connect((remote_host, remote_port))
    except Exception as e:
        print(f"[!!] Erro ao conectar no remoto {remote_host}:{remote_port}: {e}")
        client_socket.close()
        return

    if receive_first:
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)

    while True:
        # Lado Local -> Remoto
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print(f"[==>] Recebidos {len(local_buffer)} bytes do local.")
            hexdump(local_buffer)
            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)

        # Lado Remoto -> Local
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print(f"[<==] Recebidos {len(remote_buffer)} bytes do remoto.")
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)

        # Se AMBOS estiverem vazios ao mesmo tempo, significa que não há mais tráfego ativo
        # ou um dos lados fechou a conexão de forma definitiva.
        # Em proxies simples, checar se um dos lados retornou b"" (vazio real) é o sinal.
        
        # Testamos a "vivacidade" da conexão
        if not len(local_buffer) and not len(remote_buffer):
            # Pequeno delay para evitar consumo de CPU 100% em loops vazios
            import time
            time.sleep(0.1) 
            
            # Opcional: Você pode remover o 'break' e deixar o proxy vivo 
            # até que ocorra um erro de socket real (BrokenPipe)
            continue

def hexdump(src, length=16):
    if isinstance(src, bytes):
        results = []
        for i in range(0, len(src), length):
            word = src[i:i+length]
            printable = "".join([chr(b) if 0x20 <= b < 0x7F else "." for b in word])
            hexa = " ".join([f"{b:02X}" for b in word])
            hex_width = length * 3
            results.append(f"{i:04x}  {hexa:<{hex_width}}  {printable}")
        print("\n".join(results))

def receive_from(connection):
    buffer = b""
    connection.settimeout(1) # Timeout menor para ser mais responsivo
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

def request_handler(buffer):
    return buffer

def response_handler(buffer):
    return buffer

def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./building_my_own_tcp_proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5].lower() == "true"

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

if __name__ == "__main__":
    main()
