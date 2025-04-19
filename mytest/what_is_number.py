import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Вгадай число")
        self.root.geometry("400x300")

        # Згенероване число
        self.secret_number = random.randint(1, 100)
        self.attempts = 0  # лічильник спроб

        # Текст інструкції
        tk.Label(root, text="Я загадав число від 1 до 100. Вгадай!", font=("Arial", 12)).pack(pady=10)

        # Поле для вводу числа
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        # Кнопка перевірки
        tk.Button(root, text="Перевірити", font=("Arial", 12), command=self.check_guess).pack()

        # Поле для виводу результату
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        # Кнопка перезапуску гри
        tk.Button(root, text="🔄 Почати знову", font=("Arial", 10), command=self.restart_game).pack()

    def check_guess(self):
        guess_text = self.entry.get()

        if not guess_text.isdigit():
            messagebox.showwarning("Помилка", "Введи число!")
            return

        guess = int(guess_text)
        self.attempts += 1

        if guess < self.secret_number:
            self.result_label.config(text="🔽 Моє число більше!")
        elif guess > self.secret_number:
            self.result_label.config(text="🔼 Моє число менше!")
        else:
            messagebox.showinfo("🎉 Перемога!", f"Точно! Це {self.secret_number}.\nТобі знадобилось {self.attempts} спроб.")
            self.restart_game()

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()
