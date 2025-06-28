import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 7777
    client_socket.connect((host, port))
    print("listener conectado e aguardando mensagens!\n")

    while True:
        data = client_socket.recv(2048)
        message = data.strip()
        if message:
            print(f"mensagem recebida: {data.decode("utf-8")}\n")

main()