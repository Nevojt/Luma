# pip install requests pillow


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Мемогенератор")
        self.root.geometry("600x600")

        self.img_label = tk.Label(root)
        self.img_label.pack(pady=10)

        self.title_label = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=550, justify="center")
        self.title_label.pack(pady=5)

        self.button = tk.Button(root, text="Get meme 🤣", font=("Arial", 14), command=self.get_meme)
        self.button.pack(pady=20)

        self.save_button = tk.Button(root, text="💾 Save meme", font=("Arial", 12), command=self.save_meme,
                                     state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.get_meme()

    def get_meme(self):
        try:
            res = requests.get("https://meme-api.com/gimme")
            data = res.json()
            img_url = data["url"]
            title = data["title"]

            img_res = requests.get(img_url)
            img_data = Image.open(BytesIO(img_res.content))

            # змінюємо розмір для вікна
            img_data.thumbnail((500, 400))
            self.tk_img = ImageTk.PhotoImage(img_data)

            self.current_image = img_data  # Зберігаємо для подальшого збереження
            self.save_button.config(state=tk.NORMAL)  # Активуємо кнопку збереження

            self.img_label.config(image=self.tk_img)
            self.title_label.config(text=title)

        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося завантажити мем.\n{e}")

    def save_meme(self):
        if hasattr(self, 'current_image'):
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG файли", "*.png"), ("JPEG файли", "*.jpg")])
            if file_path:
                self.current_image.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = MemeApp(root)
    root.mainloop()
