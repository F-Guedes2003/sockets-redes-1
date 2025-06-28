import socket 
import threading

clients = []

def broadcast(message: str, client_socket: socket.socket):
    for client in clients:
        if client != client_socket:
            client.sendall(message.encode("utf-8"))


def handle_client(client_socket: socket.socket):
    while True:
        data = client_socket.recv(2048)
        if not data:
            break
        message = data.decode("utf-8")
        print(f"Mensagem recebida no servidor: {message}")
        broadcast(message, client_socket)
    client_socket.close()

def main():
    socket_server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host: str = "127.0.0.1"
    port: int = 7777
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind((host, port))
    socket_server.listen(5)
    print(f"Socket ounvindo no endereço: {host} | porta: {port}")

    while True:
        client_socket, adress = socket_server.accept()
        clients.append(client_socket)
        print(f"Connection is stablished from {adress}")
        print(f"connection from socket: {client_socket}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
    
    socket_server.close()

main()
