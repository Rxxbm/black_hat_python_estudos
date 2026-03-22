# BHP Net Tool - Implementação de Netcat em Python

Este projeto é uma ferramenta de rede inspirada no Netcat (o "canivete suíço" do TCP/IP), desenvolvida em Python. Ela permite realizar diversas operações de rede, como transferência de arquivos, execução de comandos remotos e criação de shells interativos.

## 🚀 Conceitos Aprendidos

Durante o desenvolvimento desta ferramenta, exploramos pilares fundamentais da programação de sistemas e redes:

1.  **Programação de Sockets (TCP/IP):**
    *   Criação de conexões cliente e servidor utilizando a biblioteca `socket`.
    *   Entendimento do fluxo de comunicação: `bind`, `listen`, `accept`, `connect`, `send` e `recv`.
    *   Diferenciação entre dados binários e strings (encodings).

2.  **Concorrência com Threading:**
    *   Uso da biblioteca `threading` para lidar com múltiplas conexões simultâneas sem bloquear o servidor principal.
    *   Cada cliente conectado ganha seu próprio "fio de execução" (thread).

3.  **Interação com o Sistema Operacional:**
    *   Uso do módulo `subprocess` para executar comandos do sistema diretamente através do Python.
    *   Captura de `stdout` e `stderr` para enviar o resultado da execução via rede.

4.  **Processamento de Argumentos de Linha de Comando:**
    *   Uso do módulo `getopt` para criar uma interface de linha de comando profissional, aceitando flags curtas e longas (ex: `-l` ou `--listen`).

5.  **Manipulação de Arquivos e I/O:**
    *   Leitura de `stdin` para envio de dados.
    *   Escrita de buffers binários em disco para funcionalidades de upload.

## 💼 Oportunidades Reais e Casos de Uso

Uma ferramenta como esta possui diversas aplicações práticas no dia a dia de profissionais de TI:

*   **Administração de Sistemas:** Executar comandos em servidores remotos de forma rápida ou transferir arquivos quando protocolos como SSH/SCP não estão disponíveis ou configurados.
*   **Debug de Rede:** Testar se portas específicas estão abertas e verificar a resposta de serviços (como banners de HTTP/SMTP).
*   **Automação de Tarefas:** Integrar a ferramenta em scripts para monitorar a disponibilidade de serviços ou coletar logs remotamente.
*   **Segurança e Pentesting (Ético):**
    *   **Reverse Shells:** Estabelecer uma conexão de volta para o atacante a partir de uma máquina alvo.
    *   **Bind Shells:** Abrir uma porta na máquina alvo que entrega um terminal de comando.
    *   **Exfiltração de Dados:** Transferir arquivos de forma discreta entre máquinas.
*   **Desenvolvimento de Ferramentas Customizadas:** Base para criar proxies simples, scanners de porta ou ferramentas de chat minimalistas.

## 🛠️ Como Usar

### Iniciar um servidor com Shell Interativo
```bash
python building_netcat.py -l -p 5555 -t 127.0.0.1 -c
```

### Conectar ao servidor
```bash
python building_netcat.py -p 5555 -t 127.0.0.1
```

### Enviar um arquivo
```bash
# No lado que recebe:
python building_netcat.py -l -p 5555 -u output.txt

# No lado que envia:
cat source.txt | python building_netcat.py -t <IP> -p 5555
```

---
*Aviso: Esta ferramenta deve ser utilizada apenas para fins educacionais e em ambientes controlados onde você possui autorização expressa.*
