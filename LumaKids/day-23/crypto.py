import tkinter as tk
from tkinter import messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Crypto")
        self.root.geometry("500x380")

        tk.Label(root, text="Write your message for crypto/decrypto:",
                 font=("Arial", 12)).pack()
        self.input_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.input_entry.pack()

        tk.Label(root, text="Shift (number):", font=("Arial", 12)).pack(pady=10)
        self.shift_entry = tk.Entry(root, width=10, font=("Arial", 12))
        self.shift_entry.pack(pady=15)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Crypto", font=("Arial", 12),
                  command=self.encrypt_text
                  ).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Decrypt", font=("Arial", 12),
                  command=self.decrypt_text).pack(side="left", padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12),
                                     fg="green", wraplength=450, justify="center")
        self.result_label.pack(pady=10)

    def encrypt_text(self):
        self.process_text(encrypt=True)

    def decrypt_text(self):
        self.process_text(encrypt=False)

    def process_text(self, encrypt=True):
        text = self.input_entry.get()
        shift_text = self.shift_entry.get()

        if not shift_text.isdigit():
            messagebox.showerror("Error", "Shift not digit")

        shift = int(shift_text)
        if not encrypt:
            shift = -shift

        result = self.caesar_cipher(text, shift)
        self.result_label.config(text=f"Result: {result}")


    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char

        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()