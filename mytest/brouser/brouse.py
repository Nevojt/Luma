# pip install tkhtmlview

import tkinter as tk
from tkhtmlview import HTMLLabel
import requests

class SimpleBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("🌐 Міні-браузер")
        self.root.geometry("800x600")

        self.history = []  # стек для назад
        self.future = []   # стек для вперед

        # Верхня панель з кнопками і URL
        top_frame = tk.Frame(root)
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        self.back_button = tk.Button(top_frame, text="⬅️", command=self.go_back, state=tk.DISABLED)
        self.back_button.pack(side=tk.LEFT)

        self.forward_button = tk.Button(top_frame, text="➡️", command=self.go_forward, state=tk.DISABLED)
        self.forward_button.pack(side=tk.LEFT)

        self.url_entry = tk.Entry(top_frame, font=("Arial", 12), width=60)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        self.url_entry.insert(0, "https://example.com")

        go_button = tk.Button(top_frame, text="Перейти", command=self.load_page)
        go_button.pack(side=tk.LEFT)

        # HTML-відображення
        self.page_area = HTMLLabel(root, html="<h3>Вітаю у браузері!</h3>", width=800, height=550)
        self.page_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def load_page(self, url=None):
        if url is None:
            url = self.url_entry.get()

        if not url.startswith("http"):
            url = "https://" + url

        # якщо ми переходимо на нову сторінку вручну — додаємо в історію
        current_url = self.url_entry.get()
        if current_url and current_url != url:
            self.history.append(current_url)
            self.back_button.config(state=tk.NORMAL)
            self.future.clear()
            self.forward_button.config(state=tk.DISABLED)

        try:
            response = requests.get(url)
            html = response.text
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.page_area.set_html(html)
        except Exception as e:
            self.page_area.set_html(f"<h3 style='color:red'>Помилка: {e}</h3>")

    def go_back(self):
        if self.history:
            self.future.append(self.url_entry.get())
            url = self.history.pop()
            self.load_page(url)
            self.forward_button.config(state=tk.NORMAL)

        if not self.history:
            self.back_button.config(state=tk.DISABLED)

    def go_forward(self):
        if self.future:
            self.history.append(self.url_entry.get())
            url = self.future.pop()
            self.load_page(url)
            self.back_button.config(state=tk.NORMAL)

        if not self.future:
            self.forward_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBrowser(root)
    root.mainloop()
