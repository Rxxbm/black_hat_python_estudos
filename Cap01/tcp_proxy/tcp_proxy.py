import sys
import socket
import threading
import argparse

# Hex dump function to see raw traffic (Updated for Python 3)
def hexdump(src: bytes, length=16) -> None:
    """Hex dump utility with Python 3 byte handling."""
    for i in range(0, len(src), length):
        word = src[i:i+length]
        printable = ''.join([chr(b) if 0x20 <= b < 0x7F else '.' for b in word])
        hexa = ' '.join([f'{b:02X}' for b in word])
        hex_width = length * 3
        print(f'{i:04X}  {hexa:<{hex_width}}  {printable}')

def receive_from(connection: socket.socket) -> bytes:
    """Read all data from the socket."""
    buffer = b""
    connection.settimeout(2)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except (TimeoutError, socket.timeout):
        pass
    return buffer

def request_handler(buffer: bytes) -> bytes:
    """Modify requests (for future expansion)."""
    # Ex: Replace headers, inject payloads, etc.
    return buffer

def response_handler(buffer: bytes) -> bytes:
    """Modify responses (for future expansion)."""
    return buffer

def proxy_handler(client_socket: socket.socket, remote_host: str, 
                  remote_port: int, receive_first: bool) -> None:
    """Handles the traffic between local client and remote host."""
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_socket:
        remote_socket.connect((remote_host, remote_port))

        if receive_first:
            remote_buffer = receive_from(remote_socket)
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            if len(remote_buffer):
                print(f"[<==] Sending {len(remote_buffer)} bytes to localhost.")
                client_socket.send(remote_buffer)

        while True:
            # Phase 1: Local -> Remote
            local_buffer = receive_from(client_socket)
            if len(local_buffer):
                print(f"[==>] Received {len(local_buffer)} bytes from localhost.")
                hexdump(local_buffer)
                local_buffer = request_handler(local_buffer)
                remote_socket.send(local_buffer)
                print(f"[==>] Sent to remote.")

            # Phase 2: Remote -> Local
            remote_buffer = receive_from(remote_socket)
            if len(remote_buffer):
                print(f"[<==] Received {len(remote_buffer)} bytes from remote.")
                hexdump(remote_buffer)
                remote_buffer = response_handler(remote_buffer)
                client_socket.send(remote_buffer)
                print(f"[<==] Sent to localhost.")

            if not len(local_buffer) or not len(remote_buffer):
                client_socket.close()
                print("[*] No more data. Closing connections.")
                break

def server_loop(local_host: str, local_port: int, 
                remote_host: str, remote_port: int, receive_first: bool) -> None:
    """Main loop to listen for connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print(f"[!!] Failed to listen on {local_host}:{local_port}")
        print(f"[!!] Error: {e}")
        sys.exit(0)

    print(f"[*] Listening on {local_host}:{local_port}")
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print(f"[>] Received connection from {addr[0]}:{addr[1]}")
        
        proxy_thread = threading.Thread(
            target=proxy_handler,
            args=(client_socket, remote_host, remote_port, receive_first)
        )
        proxy_thread.start()

def main() -> None:
    parser = argparse.ArgumentParser(description="Python 3 TCP Proxy")
    parser.add_argument("localhost", help="Local host to listen on")
    parser.add_argument("localport", type=int, help="Local port to listen on")
    parser.add_argument("remotehost", help="Remote host to connect to")
    parser.add_argument("remoteport", type=int, help="Remote port to connect to")
    parser.add_argument("--receive-first", action="store_true", help="Receive data from remote first")

    args = parser.parse_args()

    server_loop(args.localhost, args.localport, 
                args.remotehost, args.remoteport, args.receive_first)

if __name__ == "__main__":
    main()
