# pip install requests beautifulsoup4

import tkinter as tk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup

class QuoteScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📜 Парсер цитат")
        self.root.geometry("600x500")

        self.button = tk.Button(root, text="🔍 Завантажити цитати", font=("Arial", 14), command=self.load_quotes)
        self.button.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def load_quotes(self):
        self.text_area.delete(1.0, tk.END)

        try:
            res = requests.get("https://quotes.toscrape.com")
            soup = BeautifulSoup(res.text, "html.parser")
            # print(soup)
            quotes = soup.find_all("div", class_="quote")
            # print(quotes)

            for q in quotes:
                # print(q)
                text = q.find("span", class_="text").get_text()
                print(text)
                author = q.find("small", class_="author").get_text()
                self.text_area.insert(tk.END, f"💬 {text}\n👤 {author}\n\n")

        except Exception as e:
            self.text_area.insert(tk.END, f"❌ Помилка: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteScraperApp(root)
    root.mainloop()
