import tkinter as tk
from tkinter import messagebox
import json
import os
from image_window import ImageWindow

bg_color_root = "#4682B4"
bg_color_button = "#399BBF"

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        self.root.configure(bg=bg_color_root)

        # Заголовок
        tk.Label(root, text="Login Panel", font=("Helvetica", 16, "bold"), bg=bg_color_root, fg="white").pack(pady=10)

        # Ім'я користувача
        self.username_entry = self.create_entry("User Name")
        self.password_entry = self.create_entry("Password", show="*")

        # Кнопки
        tk.Button(root, text="Login", bg=bg_color_button, fg="white", width=15, command=self.login_user).pack(pady=10)
        tk.Button(root, text="Serwis", bg=bg_color_button, fg="white", width=15, command=self.login_admin).pack()

    def create_entry(self, placeholder, show=None):
        tk.Label(self.root, text=placeholder, bg=bg_color_root, fg="white").pack()
        entry = tk.Entry(self.root, show=show)
        entry.pack(pady=5)
        return entry

    def login_user(self):
        self._login("data.json", "main.py")

    def login_admin(self):
        self._login("admin.json", "setting/update.py")

    def _login(self, filepath, script_to_open):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not os.path.exists(filepath):
            messagebox.showerror("Error", f"{filepath} not found.")
            return

        with open(filepath) as file:
            users = json.load(file)

        for user in users:
            if username == user.get("username") and password == user.get("password"):
                messagebox.showinfo("Login", "Login successful")
                self.root.destroy()
                ImageWindow()
                return

        messagebox.showwarning("Error", "Invalid username or password")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
