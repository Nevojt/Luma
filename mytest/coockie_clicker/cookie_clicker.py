import tkinter as tk
import random



# Ініціалізуємо лічильник
score = 0
upgrade_cost = 20
click_power = 1
level = 1

# Функція, яка буде викликатись при кліку
def update_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    check_level()
    maybe_bonus()


def check_level():
    global level
    new_level = score // 50 + 1
    if new_level != level:
        level = new_level
        level_label.config(text=f"Level: {level} 🎉")
        window.config(bg=random.choice(["#ffe4b5", "#c0eb75", "#ffb5e0", "#a5d8ff"]))

def maybe_bonus():
    if random.randint(1, 15) == 1:
        bonus_button.pack()

def bonus_score():
    global score
    score += 10
    score_label.config(text=f"Score: {score} (+10!)")
    bonus_button.pack_forget()

def buy_upgrade():
    global score, click_power, upgrade_cost
    if score >= upgrade_cost:
        score -= upgrade_cost # Знімаємо вартість
        click_power += 1      # Збільшуємо силу кліку

        # Оновлюємо написи
        score_label.config(text=f"Score: {score}")
        upgrade_button.config(text=f"Update click (+{click_power}) | Coast: {upgrade_cost}")
        print(f"Update buyer Power click: {click_power}")
    else:
        print("Not enough points!")




# Створюємо головне вікно
window = tk.Tk()
window.title("Cookie Clicker")
window.geometry("400x450")

# Створюємо напис для рахунку
score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 24))
score_label.pack(pady=10)
level_label = tk.Label(window, text=f"Level: {level}", font=("Arial", 16))
level_label.pack()



# Завантажуємо зображення печива (файл cookie.png має бути поруч)
try:
    # Спочатку завантажуємо зображення
    cookie_image_original = tk.PhotoImage(file="cookie.png")
    cookie_image = cookie_image_original.subsample(5, 5)

except Exception:
    print("Error: file cookie.png not found")
    # Якщо зображення немає, використовуємо текст
    cookie_button = tk.Button(
        window,
        text="🍪",
        font=("Arial", 40),
        command=update_score
    )
else:
    cookie_button = tk.Button(
        window,
        image=cookie_image,
        command=update_score,
        borderwidth=0 # Прибираємо рамку кнопки
    )
cookie_button.pack()

upgrade_button = tk.Button(
    window,
    text=f"Update click | Coast: {upgrade_cost}",
    font=("Arial", 14),
    command=buy_upgrade
)
upgrade_button.pack(pady=20)

bonus_button = tk.Button(window, text="🎁 Bonus! +10", font=("Arial", 12), bg="#fff176", command=bonus_score)

# Запускаємо головний цикл програми
window.mainloop()
