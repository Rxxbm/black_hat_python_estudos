# 🚀 TCP Proxy - Black Hat Python (Modernizado)

Guia de testes para interceptação de tráfego usando seu proxy TCP.

## 🧪 Teste 1: Servidor FTP (Docker)

O FTP é ótimo para testes porque o servidor envia um banner inicial (exigindo `receive_first=True`).

### 1. Subir o servidor alvo
Use este comando (certifique-se de copiar todas as linhas ou use a versão em uma linha só abaixo):

```bash
docker run -d \
  --name ftp-alvo \
  -e FTP_USER=admin \
  -e FTP_PASS=12345 \
  -p 21:21 \
  fauria/vsftpd
```

*Versão em linha única:*
`docker run -d --name ftp-alvo -e FTP_USER=admin -e FTP_PASS=12345 -p 21:21 fauria/vsftpd`

### 2. Iniciar o seu Proxy
O proxy escutará na porta `2121` e redirecionará para a porta `21` do Docker.
```bash
python3 building_my_own_tcp_proxy.py 127.0.0.1 2121 127.0.0.1 21 True
```

### 3. Conectar o Cliente
Em outro terminal:
```bash
ftp -p 127.0.0.1 2121
```

---

## 🛠️ Teste 2: Netcat (Sem Docker)

Ideal para testes rápidos e manuais de "Mão na Massa".

### 1. Terminal 1: Servidor Alvo
```bash
nc -lk 9999
```

### 2. Terminal 2: Seu Proxy
```bash
python3 building_my_own_tcp_proxy.py 127.0.0.1 8888 127.0.0.1 9999 False
```

### 3. Terminal 3: Cliente
```bash
nc 127.0.0.1 8888
```
*Tudo que você digitar aqui passará pelo proxy e aparecerá no Terminal 1.*

---

## 📌 Notas Importantes
- **Bytes vs Strings:** O script usa `bytes`, o padrão correto para Python 3.
- **receive_first:** Use `True` para protocolos onde o servidor fala primeiro (FTP, SSH) e `False` para protocolos onde o cliente fala primeiro (HTTP).
- **Cleanup Docker:** Para parar o teste FTP: `docker stop ftp-alvo && docker rm ftp-alvo`
