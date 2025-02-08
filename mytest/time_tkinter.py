import tkinter as tk
from time import strftime


# Функція для оновлення часу та дати
def update_time():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%Y-%m-%d")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_time)


# Функція для зміни кольору тексту
def change_text_color():
    colors = ["cyan", "red", "green", "yellow", "white", "orange"]
    current_color = clock_label.cget("fg")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    clock_label.config(fg=next_color)
    date_label.config(fg=next_color)

# Функція для зміни кольору фону
def change_bg_color():
    colors = ["black", "gray", "blue", "purple", "brown", "pink"]
    current_color = clock_label.cget("bg")
    next_color = colors[(colors.index(current_color) + 1) % len(colors)]
    clock_label.config(bg=next_color)
    date_label.config(bg=next_color)
    root.config(bg=next_color)

# Створення головного вікна
root = tk.Tk()
root.title("Digital Clock")
root.config(bg="black")

# Відображення годинника
clock_label = tk.Label(root,
                       font=("Helvetica", 48),
                       bg="black", fg="cyan")
clock_label.pack(anchor="center", fill="both",
                 expand=True)


# Відображення дати
date_label = tk.Label(root,
                      font=("Helvetica", 24),
                      bg="black", fg="cyan")
date_label.pack(anchor="s", fill="both", expand=True)

# Кнопки для зміни кольорів
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=10)

text_color_button = tk.Button(button_frame,
                              text="Change Text Color",
                              command=change_text_color,
                              font=("Helvetica", 12),
                              bg="cyan", fg="black")
text_color_button.pack(side="left", padx=5)

bg_color_button = tk.Button(button_frame,
                             text="Change BG Color",
                             command=change_bg_color,
                             font=("Helvetica", 12),
                             bg="cyan", fg="black")
bg_color_button.pack(side="left", padx=5)


update_time()

root.mainloop()