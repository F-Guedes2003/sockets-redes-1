import socket

def main():
    client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host: str = "127.0.0.1"
    port: int = 7777
    client_socket.connect((host, port))

    while True:
        client_input:str = input("Enter your message: ")
        client_socket.sendall(client_input.encode("utf-8"))
    
    client_socket.close()

main()