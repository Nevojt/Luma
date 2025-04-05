import tkinter as tk
import random

class SmileGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wanted Smile")
        self.root.geometry("600x400")

        self.score = 0
        self.smiles = ["😊", "😂", "😎", "😍", "😜", "😇"]

        self.smile_button = tk.Button(root, text=";)",
                                      font=("Arial", 24),
                                      command=self.catch_smile)
        self.score_label = tk.Label(root, text="Score: 0",
                                    font=("Arial", 14))
        self.score_label.pack()

        self.move_smile()

    def move_smile(self):
        x = random.randint(50, 550)
        y = random.randint(50, 350)
        self.smile_button.place(x=x, y=y)
        self.root.after(2000, self.move_smile)

    def catch_smile(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        new_smile = random.choice(self.smiles)
        self.smile_button.config(text=new_smile)
        self.move_smile()





if __name__ == "__main__":
    root = tk.Tk()
    game = SmileGame(root)
    root.mainloop()