
import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("What is the number?")
        self.root.geometry("400x300")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        tk.Label(root, text="What guess number 1 - 100?",
                 font=("Arial, 14")).pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial, 14"), justify="center")
        self.entry.pack(pady=10)

        tk.Button(root, text="Check", font=("Arial, 14"),
                  command=self.check_guess,
                  bg="pink"
                  ).pack()

        self.result_label = tk.Label(root, text="", font=("Arial, 14"))
        self.result_label.pack(pady=20)

        tk.Button(root, text="Restart now", font=("Arial, 14"),
                  bg="green",
                  command=self.restart_game
                  ).pack()

    def check_guess(self):
        guess_text = self.entry.get()

        if not guess_text.isdigit():
            messagebox.showwarning("Error", "Input number")
            return

        guess = int(guess_text)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="My number is biggest!!!")
        elif guess > self.secret_number:
            self.result_label.config(text="My number is small!!")
        else:
            messagebox.showinfo("Win", f"Yes! It is {self.secret_number}.\nYou attempts {self.attempts} ")
            self.restart_game()

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")










if __name__ == "__main__":
    root =tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()