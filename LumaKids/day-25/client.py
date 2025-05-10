import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

HOST = '192.168.0.145'
PORT = 5555

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-chat")

#         History chat
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10)

#         Input message
        self.msg_entry = tk.Entry(root, width=50)
        self.msg_entry.pack(padx=10, pady=5, side=tk.LEFT)

#         Button send message
        tk.Button(root, text="Sent",
                  command=self.send_message
                  ).pack(padx=10, pady=5, side=tk.LEFT)

#         Connect to server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((HOST, PORT))
        except:
            messagebox.showerror("Error", "Could not connect to the server.")
            exit(0)

#         Nickname
        self.nickname = simpledialog.askstring("Nickname", "Enter your nickname")
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