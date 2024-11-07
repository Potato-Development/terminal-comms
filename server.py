import socket
import threading
HOST = '127.0.0.1'  
PORT = 5000
clients = []  
nicknames = []  

def broadcast(message, client):
    """Send a message to all clients except the sender."""
    for c in clients:
        if c != client:
            try:
                c.send(message)
            except:
                # Handle potential disconnections
                clients.remove(c)
                nicknames.remove(nicknames[clients.index(c)])

def handle(client):
    """Handle client communication."""
    try:
        while True:
            message = client.recv(1024)
            if message:
                print(f"Message received: {message.decode('utf-8')}")
                broadcast(message, client)
    except:
        index = clients.index(client)
        clients.remove(client)
        nickname = nicknames[index]
        broadcast(f"{nickname} has left the chat.".encode('utf-8'), client)
        print(f"{nickname} disconnected.")
        nicknames.remove(nickname)
        client.close()

def receive():
    """Accept incoming client connections."""
    server.listen()
    print(f"Server running on {HOST}:{PORT}...")

    while True:
        client, address = server.accept()
        print(f"Connection from {address} established.")
        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}.")
        broadcast(f"{nickname} has joined the chat.".encode('utf-8'), client)
        client.send(f"Welcome {nickname}!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Start receiving clients
receive()