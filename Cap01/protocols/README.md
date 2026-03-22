# Protocolos de Rede e Programação de Sockets com Python

Este diretório contém exemplos práticos de como implementar clientes e servidores básicos utilizando os protocolos **TCP** e **UDP** através da biblioteca `socket` do Python.

## Conceitos Aprendidos

### 1. Sockets
Um **socket** é o ponto de extremidade de um link de comunicação bidirecional entre dois programas que rodam na rede. Em Python, a biblioteca `socket` fornece acesso à interface de rede do sistema operacional.

### 2. TCP (Transmission Control Protocol)
Implementado nos arquivos `simple_tcp_client.py`, `simple_tcp_server.py` e `ex01.py`.
- **Tipo de Socket:** `socket.SOCK_STREAM`.
- **Características:**
    - **Orientado à Conexão:** Exige que uma conexão seja estabelecida (handshake) antes da troca de dados.
    - **Confiabilidade:** Garante que os dados cheguem na ordem correta e sem erros. Se um pacote for perdido, ele é retransmitido.
    - **Fluxo:** Utiliza métodos como `connect()` no cliente e `listen()`/`accept()` no servidor.

### 3. UDP (User Datagram Protocol)
Implementado nos arquivos `simple_udp_client.py` e `simple_udp_server.py`.
- **Tipo de Socket:** `socket.SOCK_DGRAM`.
- **Características:**
    - **Sem Conexão:** Não há handshake. Os pacotes (datagramas) são enviados diretamente para o destino.
    - **Velocidade:** Mais rápido que o TCP por não ter a sobrecarga de controle de conexão.
    - **Não Confiável:** Não garante a entrega nem a ordem dos pacotes. É ideal para streaming de vídeo ou jogos online.
    - **Métodos:** Utiliza `sendto()` e `recvfrom()` que especificam/recebem o endereço de destino em cada operação.

### 4. Arquitetura Cliente-Servidor
- **Servidor:** Precisa se vincular (`bind`) a um endereço IP e uma porta específica para "ouvir" requisições. No caso do TCP, ele aceita conexões (`accept`).
- **Cliente:** Inicia a comunicação conectando-se ao endereço e porta do servidor.

### 5. Multi-threading em Servidores
Como visto em `simple_tcp_server.py`, para que um servidor TCP possa atender múltiplos clientes simultaneamente sem bloquear, utilizamos a biblioteca `threading`. Cada nova conexão aceita (`accept`) dispara uma nova thread para processar as mensagens daquele cliente específico.

### 6. Boas Práticas e Segurança
- **Portas Altas:** Portas abaixo de 1024 (como a 80) são reservadas e exigem privilégios de administrador (root/sudo) no Linux para serem vinculadas. Por isso, nos exemplos, preferimos portas como 9999.
- **Codificação:** Dados transmitidos pela rede devem ser convertidos para bytes (`.encode()` e `.decode()`).

## Como Executar
1. Inicie um servidor em um terminal:
   ```bash
   python3 simple_tcp_server.py
   ```
2. Execute o cliente correspondente em outro terminal:
   ```bash
   python3 simple_tcp_client.py
   ```
