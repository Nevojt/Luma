import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import  requests
from io import BytesIO


class MemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memes Generations")
        self.root.geometry("600x600")

        self.img_label = tk.Label(root)
        self.img_label.pack(pady=10)

        self.title_label = tk.Label(root, text="", font=("Arial", 12, "bold"),
                                    wraplength=550, justify="center")
        self.title_label.pack(pady=5)

        self.button = tk.Button(root, text="Get meme", font=("Arial", 12, "bold"),
                                command=self.get_meme)
        self.button.pack(pady=5)

        self.get_meme()


    def get_meme(self):
        try:
            res = requests.get("https://meme-api.com/gimme")
            data = res.json()
            img_url = data["url"]
            title = data["title"]

            img_res = requests.get(img_url)
            img_date = Image.open(BytesIO(img_res.content))

            img_date.thumbnail((500, 400))
            self.tk_img = ImageTk.PhotoImage(img_date)

            # self.current_image = img_date
#           self.save_butto.config(state=tk.NORMAL)

            self.img_label.config(image=self.tk_img)
            self.title_label.config(text=title)

        except Exception as e:
            messagebox.showerror("Error", f"Dont download image \n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemeApp(root)
    root.mainloop()