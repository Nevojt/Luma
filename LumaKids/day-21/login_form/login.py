import tkinter as tk
from tkinter import messagebox
import json
import os


bg_color_root = "blue"
bg_color_button = "green"


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        self.root.configure(bg=bg_color_root)

        tk.Label(root, text="Login Panel",
                 font=("Helvetica", 16, "bold"),
                 bg=bg_color_root,
                 fg="white").pack(pady=10)

        self.username_entry = self.create_entry("User Name")
        self.password_entry = self.create_entry("Password", show="*")

        tk.Button(root, text="Login",
                  bg=bg_color_button, fg="white",
                  width=15,
                  command=self.login_user).pack(pady=10)


    def create_entry(self, placeholder, show=None):
        tk.Label(self.root, text=placeholder,
                 bg=bg_color_root, fg="white").pack()
        entry = tk.Entry(self.root, show=show)
        entry.pack(pady=5)
        return entry

    def login_user(self):
        self._login("data.json")

    def _login(self, filepath):
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
                return

        messagebox.showwarning("Error", "Invalid username or password.")



if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()