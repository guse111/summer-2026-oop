import socket
import threading

class ChatServerSync:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host = host
        self.port = port
        # Создаем "сырой" сокет
        # AF_INET = IPv4, SOCK_STREAM = TCP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Разрешаем повторное использование порта (если сервер упал и перезапустился)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        """Запуск сервера"""
        # Привязываем сокет к адресу и порту
        self.server_socket.bind((self.host, self.port))
        
        # Начинаем слушать подключения (5 - размер очереди ожидающих клиентов)
        self.server_socket.listen(5)
        print(f"Сервер запущен на {self.host}:{self.port} ...")
        
        try:
            while True:
                # accept() блокирует выполнение, пока не подключится клиент
                # Возвращает НОВЫЙ сокет для общения с этим клиентом и его адрес
                client_socket, addr = self.server_socket.accept()
                print(f"[+] Новое подключение от {addr}")
                
                # Запускаем обработку клиента в отдельном потоке
                # (иначе один клиент заблокирует всех остальных!)
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, addr)
                )
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\nСервер остановлен")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, addr):
        """
        Обработка одного клиента.
        Эта функция выполняется в ОТДЕЛЬНОМ потоке для каждого клиента.
        """
        try:
            while True:
                # recv() блокирует выполнение, пока не придут данные
                # 1024 - максимальный размер буфера для чтения за раз
                data = client_socket.recv(1024)
                
                if not data:
                    # Клиент отключился
                    break
                
                # Декодируем байты в строку
                message = data.decode('utf-8').strip()
                print(f"[{addr}] {message}")
                
        except ConnectionResetError:
            print(f"[!] Клиент {addr} резко отключился")
        finally:
            print(f"[-] Клиент {addr} отключился")
            client_socket.close()

if __name__ == '__main__':
    server = ChatServerSync()
    server.start()