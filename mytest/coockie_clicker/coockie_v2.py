import tkinter as tk
import random

score = 0
upgrade_cost = 20
click_power = 1
level = 1

def update_score():
    global score
    score += click_power
    score_label.config(text=f"Score: {score}")
    animate_cookie()
    check_level()
    maybe_bonus()
    if score >= upgrade_cost:
        upgrade_button.config(state="normal")
    else:
        upgrade_button.config(state="disabled")

def buy_upgrade():
    global score, click_power, upgrade_cost
    if score >= upgrade_cost:
        score -= upgrade_cost
        click_power += 1
        upgrade_cost += 15
        upgrade_button.config(text=f"Update click (+{click_power}) | Cost: {upgrade_cost}")
        score_label.config(text=f"Score: {score}")

def check_level():
    global level
    new_level = score // 50 + 1
    if new_level != level:
        level = new_level
        level_label.config(text=f"Level: {level} 🎉")
        window.config(bg=random.choice(["#ffe4b5", "#c0eb75", "#ffb5e0", "#a5d8ff"]))

def animate_cookie():
    cookie_button.config(font=("Arial", 50))
    window.after(100, lambda: cookie_button.config(font=("Arial", 40)))

def maybe_bonus():
    if random.randint(1, 15) == 1:
        bonus_button.pack()

def bonus_score():
    global score
    score += 10
    score_label.config(text=f"Score: {score} (+10!)")
    bonus_button.pack_forget()

window = tk.Tk()
window.title("Cookie Clicker")
window.geometry("400x450")

score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 24))
score_label.pack(pady=10)
level_label = tk.Label(window, text=f"Level: {level}", font=("Arial", 16))
level_label.pack()

cookie_image_original = tk.PhotoImage(file="cookie.png")
cookie_image = cookie_image_original.subsample(5, 5)
cookie_button = tk.Button(window, image=cookie_image, command=update_score)
cookie_button.pack()

bonus_button = tk.Button(window, text="🎁 Bonus! +10", font=("Arial", 12), bg="#fff176", command=bonus_score)

upgrade_button = tk.Button(window, text=f"Update click | Cost: {upgrade_cost}", font=("Arial", 14), command=buy_upgrade, state="disabled")
upgrade_button.pack(pady=20)

window.mainloop()
