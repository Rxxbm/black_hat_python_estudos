# 🐍 Black Hat Python - Caderno de Estudos

Este repositório contém meus estudos, anotações e implementações baseadas no livro **"Black Hat Python"** de Justin Seitz e Tim Arnold. O objetivo deste projeto é explorar as capacidades do Python para segurança ofensiva, ferramentas de rede e automação de tarefas de hacking ético.

---

## 🚀 O que este repositório contém?

O projeto está organizado por capítulos e temas, facilitando o aprendizado progressivo.

### 📁 [Cap01 - Fundamentos de Rede](./Cap01)
Neste capítulo inicial, mergulhamos nos conceitos básicos de sockets e protocolos de transporte.

*   **[Protocolos de Rede](./Cap01/protocols):** Implementações básicas de clientes e servidores TCP e UDP.
*   **[Replacing Netcat](./Cap01/replacing_netcat):** Construção de uma ferramenta similar ao `netcat` do zero, suportando execução de comandos remotos, upload de arquivos e reverse shells.
*   **[TCP Proxy](./Cap01/tcp_proxy):** Um proxy TCP funcional capaz de interceptar, modificar e encaminhar tráfego entre um cliente e um servidor alvo.

---

## 🛠️ Tecnologias e Conceitos Explorados

*   **Python 3.10+:** Uso de f-strings, type hinting e gerenciadores de contexto (`with`).
*   **Socket Programming:** Manipulação de fluxos de dados em baixo nível (TCP/UDP).
*   **Threading:** Processamento paralelo para gerenciar múltiplas conexões simultâneas.
*   **Subprocess:** Interação com o sistema operacional para execução de comandos remotos.
*   **Docker:** Utilizado para criar ambientes de teste isolados (ex: servidores FTP para testes de proxy).

---

## 🛡️ Ética e Responsabilidade

Todas as ferramentas e técnicas demonstradas aqui são para fins **exclusivamente didáticos**. Use este conhecimento para fortalecer sistemas e entender como as ameaças funcionam. Nunca execute esses scripts contra sistemas que você não possui autorização explícita para testar.

---

## ⚙️ Como Começar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/black_hat_python.git
    cd black_hat_python
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Explore as pastas:**
    Cada diretório contém seu próprio `README.md` com instruções específicas de execução e testes.

---

## 📚 Referências
*   Livro: [Black Hat Python, 2nd Edition](https://nostarch.com/black-hat-python2e)
*   Documentação Oficial: [Python socket](https://docs.python.org/3/library/socket.html)

---
*Desenvolvido com 🐍 por [Seu Nome/Rubem]*
