import socket
HOST = '0.0.0.0'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("Socket server is running and waiting for connections...")
while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    if data:
        message = data.decode()
        print(f"Received: {message}")
        reply = f"Server received: {message}"
        conn.sendall(reply.encode())
    conn.close()
