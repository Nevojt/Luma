import socket
import threading

HOST = '0.0.0.0'  # приймати з усіх IP
PORT = 5555

clients = []  # список пар (socket, nickname)

def handle_client(client_socket):
    try:
        # 1. Спочатку чекаємо на повідомлення з нікнеймом
        nickname_data = client_socket.recv(1024).decode('utf-8')
        if nickname_data.startswith("/nickname "):
            nickname = nickname_data.replace("/nickname ", "").strip()
        else:
            nickname = "Безіменний"

        # 2. Лише тепер додаємо у список
        clients.append((client_socket, nickname))

        # 3. Сповіщаємо всіх
        broadcast(f"🔔 {nickname} приєднався до чату!", sender_socket=None)

        # 4. Основний цикл прийому повідомлень
        while True:
            msg = client_socket.recv(1024).decode('utf-8')
            broadcast(msg, sender_socket=client_socket)

    except Exception as e:
        print(f"Помилка: {e}")
        remove_client(client_socket)


def broadcast(msg, sender_socket):
    for client_socket, _ in clients:
        # if client_socket != sender_socket:
        client_socket.send(msg.encode('utf-8'))

def remove_client(client_socket):
    for client in clients:
        if client[0] == client_socket:
            clients.remove(client)
            client_socket.close()
            break




def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Сервер запущено на {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Підключено: {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
