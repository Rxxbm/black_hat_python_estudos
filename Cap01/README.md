# Capítulo 01: Fundamentos de Redes com Python

Este capítulo aborda os conceitos essenciais de rede necessários para construir ferramentas de segurança. O foco principal é entender como os protocolos **TCP** e **UDP** funcionam na prática através da manipulação de **Sockets**.

## Conteúdo do Capítulo

1.  **[Protocolos de Rede](./protocols/):**
    *   Clientes e Servidores TCP.
    *   Clientes e Servidores UDP.
    *   Gerenciamento de conexões com threads.

2.  **[Construindo seu próprio Netcat](./replacing_netcat/):**
    *   Implementação de uma ferramenta CLI versátil para comunicação de rede.
    *   Funcionalidades de execução de comandos remotos (shell).
    *   Transferência de arquivos entre máquinas.

3.  **[TCP Proxy](./tcp_proxy/):**
    *   Criação de um intermediário para capturar e analisar tráfego de rede.
    *   Modificação de pacotes em tempo real.
    *   Simulação de ataques Man-in-the-Middle (MITM) para fins de debug e estudo.

## Conceitos Chave

*   **Socket Programming:** A base de toda comunicação em rede.
*   **Concorrência:** Uso de threads para suportar múltiplos clientes.
*   **I/O de Baixo Nível:** Manipulação de fluxos de bytes.

---
*Estes exemplos seguem os padrões de modernização do Python 3.10+, garantindo código limpo e eficiente.*
