import socket
import threading

HOST = '127.0.0.1'  
PORT = 65432    
NAME = "Анастасія"     
SURNAME = "Харитонова"  
VALID_LOGIN = "me"    
VALID_PASSWORD = "1234"

class Server:
    def __init__(self, mode):
        self.mode = mode
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)
        print(f"Сервер запущено на {HOST}:{PORT}")

    def handle_client(self, client_socket, address):
        print(f"Підключився клієнт {address}")
        try:
            data = client_socket.recv(1024).decode('utf-8')
            login, password = data.split(',')
            
            if login == VALID_LOGIN and password == VALID_PASSWORD:
                response = f"Вітаю, {NAME} {SURNAME}! Ваш логін: {VALID_LOGIN}, ваш пароль: {VALID_PASSWORD}."
            else:
                response = "Невірний логін або пароль."
            
            client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Помилка: {e}")
        finally:
            client_socket.close()
            print(f"Клієнт {address} відключився")

    def start_sequential(self):
        while True:
            client_socket, address = self.server_socket.accept()
            self.handle_client(client_socket, address)

    def start_parallel(self):
        while True:
            client_socket, address = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            thread.start()

    def start(self):
        if self.mode == '1':
            self.start_sequential()
        elif self.mode == '2':
            self.start_parallel()


if __name__ == "__main__":
    mode = input("Введіть режим роботи сервера (1 - послідовний, 2 - паралельний): ").strip()
    server = Server(mode)
    server.start()
