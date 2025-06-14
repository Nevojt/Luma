import tkinter as tk
import random
import time

score = 0
super_score = 0
start_time = None
best_reaction = None
is_supercat = False
is_superbonus_visible = False  # <--- прапорець

window = tk.Tk()
window.title("Catch the cat!")
window.geometry("800x800")

score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 18))
score_label.pack()

super_score_label = tk.Label(window, text=f"Super score: {super_score}", font=("Arial", 18))
super_score_label.pack()

reaction_label = tk.Label(window, text="Current reaction time: ---", font=("Arial", 14))
reaction_label.pack()

best_label = tk.Label(window, text="The best time: ---", font=("Arial", 14))
best_label.pack()

bonus_label = tk.Label(window, text="", font=("Arial", 18), fg="red")
bonus_label.pack()

super_bonus_label = tk.Label(window, text="", font=("Arial", 18), fg="purple")
super_bonus_label.pack()

# Картинки для звичайних котиків
cat_images = []
for name in ["cat1.png", "cat2.png", "cat3.png", "cat4.png", "cat5.png"]:
    img = tk.PhotoImage(file=name).subsample(5, 5)
    cat_images.append(img)

# Картинка для супер-котика
supercat_image = tk.PhotoImage(file="super_cat.png").subsample(5, 5)
# Картинка для супер-бонусного котика
superbonus_image = tk.PhotoImage(file="super_cat_bonus.png").subsample(8, 8)

bad_cat_image = tk.PhotoImage(file="bad_cat.png").subsample(5, 5)

def move_bug():
    global start_time, is_supercat
    if random.randint(1, 8) == 1:
        cat.config(image=supercat_image)
        cat.image = supercat_image
        is_supercat = True
    else:
        random_cat = random.choice(cat_images)
        cat.config(image=random_cat)
        cat.image = random_cat
        is_supercat = False
    cat.place(x=random.randint(0, 730), y=random.randint(80, 730))
    start_time = time.time()

def catch_bug():
    global score, start_time, best_reaction, is_supercat
    reaction = round((time.time() - start_time) * 1000)
    if is_supercat:
        score += 5
        bonus_label.config(text="БОНУС! +5 🐾")
        window.after(500, lambda: bonus_label.config(text=""))
    else:
        score += 1
        bonus_label.config(text="")
    score_label.config(text=f"Score: {score}")
    reaction_label.config(text=f"Поточний час реакції: {reaction} мс")
    if (best_reaction is None) or (reaction < best_reaction):
        best_reaction = reaction
        best_label.config(text=f"Найкращий час: {best_reaction} мс")
    move_bug()

# --- Супер-Бонусний котик ---
def show_superbonus_cat():
    global is_superbonus_visible
    superbonus_button.place(x=random.randint(0, 730), y=random.randint(80, 730))
    is_superbonus_visible = True
    window.after(800, hide_superbonus_cat)  # Ховаємо через 0.5 сек
    window.after(random.randint(1500, 3000), show_superbonus_cat)

def hide_superbonus_cat():
    global is_superbonus_visible
    superbonus_button.place_forget()
    is_superbonus_visible = False

def catch_superbonus_cat():
    global score, super_score, is_superbonus_visible
    if is_superbonus_visible:  # щоб не клікати "в повітря"
        score += 10
        super_score += 1
        super_bonus_label.config(text="СУПЕР-БОНУС! +10 🌟")
        score_label.config(text=f"Score: {score}")
        super_score_label.config(text=f"Super score: {super_score}")
        superbonus_button.place_forget()
        is_superbonus_visible = False
        window.after(600, lambda: super_bonus_label.config(text=""))


# --- Bad cat ---
def show_bad_cat():
    global is_superbonus_visible
    bad_cat_button.place(x=random.randint(0, 730), y=random.randint(80, 730))
    is_superbonus_visible = True
    window.after(800, hide_bad_cat)  # Ховаємо через 0.5 сек
    window.after(random.randint(1500, 3000), show_bad_cat)

def hide_bad_cat():
    global is_superbonus_visible
    bad_cat_button.place_forget()
    is_superbonus_visible = False

def catch_bad_cat():
    global score, super_score, is_superbonus_visible
    if is_superbonus_visible:  # щоб не клікати "в повітря"
        score = score // 2
        super_score = 0
        super_bonus_label.config(text="BAD CAT CATCH", fg="red", font=("Arial", 25))
        score_label.config(text=f"Score: {score}")
        super_score_label.config(text=f"Super score: {super_score}")
        bad_cat_button.place_forget()
        is_superbonus_visible = False
        window.after(600, lambda: super_bonus_label.config(text=""))

# --- Головна кнопка-котик ---
cat = tk.Button(window, image=cat_images[0], command=catch_bug)
cat.place(x=200, y=200)

# --- Супер-бонусний котик-кнопка ---
superbonus_button = tk.Button(window, image=superbonus_image, command=catch_superbonus_cat, borderwidth=0)
# --- Bad Cat Button ---
bad_cat_button = tk.Button(window, image=bad_cat_image, command=catch_bad_cat, borderwidth=0)

move_bug()
window.after(random.randint(2000, 4000), show_superbonus_cat)  # Перший раз через 2–4 сек
window.after(random.randint(2000, 4000), show_bad_cat)  # Перший раз через 2–4 сек

window.mainloop()
