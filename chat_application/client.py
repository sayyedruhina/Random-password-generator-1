import socket

host = '127.0.0.1'
port = 5000

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to server!")

    while True:
        message = input("You (Client): ")

        if message.lower() == "exit":
            client_socket.send("exit".encode())
            print("Closing client...")
            break

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        if data.lower() == "exit":
            print("Server closed the chat.")
            break

        print("Server:", data)

    client_socket.close()

if __name__ == "__main__":
    start_client()