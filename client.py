
import socket
import threading


# Make sure that these settings are the same as the server's
# This is the default debug setting
HOST = '127.0.0.1'
PORT = 5000

def receive_messages(client):
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection lost.")
            client.close()
            break
def send_messages(client):
    
    while True:
        message = input('')
        client.send(message.encode('utf-8'))
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    nickname = input("Enter your nickname: ")
    client.send(nickname.encode('utf-8'))

    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

   
    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()
