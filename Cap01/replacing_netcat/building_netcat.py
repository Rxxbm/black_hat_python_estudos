import sys
import socket
import getopt
import threading
import subprocess

# Define as variáveis globais
listen             = False
command            = False
upload             = False
execute            = ""
target             = ""
upload_destination = ""
port               = 0

def usage():
    print("BHP Net Tool - Substituto do Netcat em Python")
    print()
    print("Uso: building_netcat.py -t target_host -p port")
    print("-l --listen                - escuta em [host]:[port] por conexões de entrada")
    print("-e --execute=arquivo_exec  - executa o arquivo ao receber uma conexão")
    print("-c --command               - inicializa um shell de comando (shell interativo)")
    print("-u --upload=destino        - ao receber uma conexão, faz o upload de um arquivo e escreve em [destino]")
    print()
    print()
    print("Exemplos: ")
    print("building_netcat.py -t 192.168.0.1 -p 5555 -l -c")
    print("building_netcat.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("building_netcat.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./building_netcat.py -t 192.168.0.1 -p 135")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    # Lê as opções da linha de comando
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", 
                                   ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Opção Não Tratada"

    # Vamos escutar ou apenas enviar dados pelo stdin?
    if not listen and len(target) and port > 0:
        # Lê o buffer da linha de comando
        # Isso irá bloquear, então envie CTRL-D se não estiver enviando dados via pipe
        print("[*] Lendo do stdin... (Pressione CTRL-D para finalizar a entrada)")
        buffer = sys.stdin.read()

        # Envia os dados
        client_sender(buffer)

    # Iremos escutar e potencialmente fazer upload de arquivos, executar comandos
    # ou abrir um shell de comando, dependendo das opções acima
    if listen:
        server_loop()

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta ao host alvo
        client.connect((target, port))

        if len(buffer):
            client.send(buffer.encode())

        while True:
            # Agora aguarda o retorno dos dados
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data.decode(errors="ignore")

                if recv_len < 4096:
                    break

            print(response, end="")

            # Aguarda mais entrada de dados do usuário
            buffer = input("")
            buffer += "\n"

            # Envia os dados
            client.send(buffer.encode())

    except Exception as e:
        print(f"[*] Exceção! Saindo. Erro: {e}")
        client.close()

def server_loop():
    global target
    global port

    # Se nenhum alvo for definido, escutamos em todas as interfaces
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    print(f"[*] Escutando em {target}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Conexão aceita de: {addr[0]}:{addr[1]}")

        # Cria uma thread para lidar com o novo cliente
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def run_command(command):
    # Remove a quebra de linha
    command = command.rstrip()

    # Executa o comando e obtém a saída de retorno
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except Exception:
        output = b"Falha ao executar o comando.\r\n"

    # Envia a saída de volta para o cliente
    return output

def client_handler(client_socket):
    global upload_destination
    global execute
    global command

    # Verifica se há upload de arquivo
    if len(upload_destination):
        # Lê todos os bytes e escreve no destino
        file_buffer = b""

        # Continua lendo dados até que não haja mais nada disponível
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

        # Agora tentamos gravar esses bytes no arquivo
        try:
            with open(upload_destination, "wb") as file_descriptor:
                file_descriptor.write(file_buffer)

            # Confirma que o arquivo foi gravado
            client_socket.send(f"Arquivo salvo com sucesso em {upload_destination}\r\n".encode())
        except Exception as e:
            client_socket.send(f"Falha ao salvar o arquivo em {upload_destination}\r\n Erro: {e}".encode())

    # Verifica a execução de comando
    if len(execute):
        # Executa o comando
        output = run_command(execute)
        client_socket.send(output)

    # Entra em outro loop se um shell de comando foi solicitado
    if command:
        while True:
            # Exibe um prompt simples
            client_socket.send(b"<BHP:#> ")

            # Agora recebemos dados até encontrar um linefeed (tecla enter)
            cmd_buffer = b""
            while b"\n" not in cmd_buffer:
                data = client_socket.recv(1024)
                if not data:
                    break
                cmd_buffer += data
            
            if not cmd_buffer:
                break

            # Obtém a saída do comando
            response = run_command(cmd_buffer.decode())

            # Envia a resposta de volta
            client_socket.send(response)
        
        client_socket.close()

if __name__ == "__main__":
    main()
