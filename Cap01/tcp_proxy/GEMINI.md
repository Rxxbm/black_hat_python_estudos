# Guia de Estudo: Black Hat Python (Modernizado)

Este guia serve como bússola para converter e otimizar os scripts do livro "Black Hat Python" para as versões mais recentes do Python (3.10+).

## 🛠️ Mandatos de Modernização

Ao converter scripts, priorize sempre estas construções:

### 1. F-Strings (Python 3.6+)
Substitua `%` e `.format()` por f-strings para clareza e performance.
- **Antigo:** `print "[*] Listening on %s:%d" % (local_host, local_port)`
- **Novo:** `print(f"[*] Listening on {local_host}:{local_port}")`

### 2. Tipagem Estática (Type Hinting)
Sempre defina tipos para funções para facilitar o debug e a leitura.
- **Exemplo:** `def proxy_handler(client_socket: socket.socket, remote_host: str) -> None:`

### 3. Context Managers (`with`)
Sempre utilize `with` para garantir o fechamento de sockets e arquivos.
- **Exemplo:**
  ```python
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host, port))
  ```

### 4. Byte Manipulation
Em Python 3, a distinção entre `str` (Unicode) e `bytes` é rigorosa.
- Utilize `.encode()` para enviar e `.decode()` para receber.
- Para hex dumps, utilize o método moderno `binascii.hexlify()` ou f-strings formatadas.

### 5. Asyncio (Opcional, mas recomendado)
Para proxies de alta performance, considere trocar o módulo `threading` por `asyncio`.

## 🛡️ Segurança e Ética
1. **Ambiente Controlado:** Execute scripts apenas em redes/máquinas virtuais de sua propriedade.
2. **Sanitização:** Valide inputs de linha de comando usando `argparse` em vez de manipular `sys.argv` diretamente.
3. **Dependências:** Utilize `pipenv` ou `venv` para isolar bibliotecas de terceiros como `scapy`.

## 📚 Referências Rápidas
- [Documentação Oficial do Python (Networking)](https://docs.python.org/3/library/socket.html)
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [OWASP Python Security](https://cheatsheetseries.owasp.org/cheatsheets/Python_Security_Cheat_Sheet.html)
