import socket

host = '127.0.0.1'
port = 5000

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        data = conn.recv(1024).decode()

        if data.lower() == "exit":
            print("Client closed the chat.")
            conn.send("exit".encode())
            break

        print("Client:", data)
        message = input("You (Server): ")

        if message.lower() == "exit":
            conn.send("exit".encode())
            print("Closing server...")
            break

        conn.send(message.encode())

    conn.close()

if __name__ == "__main__":
    start_server()