import socket
import json

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024)
    dictionary = json.loads(data)
    print(dictionary)
    client_socket.close()

def send_data(dictionary):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 12345))
        data = json.dumps(dictionary)
        client_socket.send(data.encode())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
