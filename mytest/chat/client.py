import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

# ifconfig
HOST = '192.168.0.66'  # IP сервера (можна змінити на локальну IP, наприклад 192.168.x.x)
PORT = 5555

# wlp0s20f3 HOST = '192.168.0.66'

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-chat 🗨️")

        # Поле для історії чату
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

        # Поле для вводу повідомлення
        self.msg_entry = tk.Entry(root, width=50)
        self.msg_entry.pack(padx=10, pady=5, side=tk.LEFT)

        tk.Button(root, text="Sent", command=self.send_message).pack(padx=10, pady=5, side=tk.LEFT)

        # Підключення до сервера
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((HOST, PORT))
        except:
            messagebox.showerror("Error", "Could not connect to the server.")
            exit(0)

        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname:")
        # ПІСЛЯ вибору ніка - одразу надсилаємо його на сервер
        self.client.send(f"/nickname {self.nickname}".encode('utf-8'))

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            full_msg = f"{self.nickname}: {msg}"
            self.client.send(full_msg.encode('utf-8'))
            self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                msg = self.client.recv(1024).decode('utf-8')
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, msg + '\n')
                self.chat_area.yview(tk.END)
                self.chat_area.config(state='disabled')
            except:
                print("Disconnected from the server.")
                self.client.close()
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()
