import tkinter as tk
import time

running = False
start_time = None
elapsed_time = 0

def start():
    global running, start_time, elapsed_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time

def stop():
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time.time() - start_time

def reset():
    global running, start_time, elapsed_time
    running = False
    start_time = None
    elapsed_time = 0
    label.config(text="00:00:00")

def update_timer():
    global elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    root.after(100, update_timer)

root = tk.Tk()
root.title("Секундомір")

label = tk.Label(root, text="00:00:00", font=("Helvetica", 30))
label.pack()

start_button = tk.Button(root, text="Старт", command=start)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(root, text="Стоп", command=stop)
stop_button.pack(side=tk.LEFT)

reset_button = tk.Button(root, text="Скинути", command=reset)
reset_button.pack(side=tk.LEFT)

update_timer()

root.mainloop()
