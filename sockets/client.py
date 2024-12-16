import socket

HOST = input("Введіть IP сервера: ")  
PORT = 65432  
class Client:
    def __init__(self):
        self.login = ""
        self.password = ""

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            
            self.login = input("Введіть логін: ")
            self.password = input("Введіть пароль: ")
            
            client_socket.sendall(f"{self.login},{self.password}".encode('utf-8'))
            
            response = client_socket.recv(1024).decode('utf-8')
            print(response)

if __name__ == "__main__":
    client = Client()
    client.connect()
