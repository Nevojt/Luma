import tkinter as tk
from PIL import Image, ImageTk


class ImageWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome")
        # self.root.geometry("500x400")

        # Заміни "your_image.png" на свою назву файлу
        image = Image.open("access.png")
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.root, image=photo)
        label.image = photo  # Зберігаємо посилання, щоб не вилетіло
        label.pack(expand=True)

        self.root.mainloop()


if __name__ == "__main__":
    ImageWindow()
