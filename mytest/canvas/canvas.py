import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Painter")
        self.root.geometry("1000x1000")

        self.color = "black"
        self.brush_size = 3

        # Полотно для малювання
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Події миші
        self.canvas.bind("<B1-Motion>",
                         self.draw
                         )

        # Панель керування
        control_frame = tk.Frame(root)
        control_frame.pack(pady=5)

        tk.Button(control_frame, text="Black", command=lambda: self.set_color("black")).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Red", command=lambda: self.set_color("red")).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Blue", command=lambda: self.set_color("blue")).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Green", command=lambda: self.set_color("green")).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Clear", command=self.clear_canvas).pack(side=tk.LEFT, padx=10)

        # Слайдер розміру
        size_frame = tk.Frame(root)
        size_frame.pack(pady=5)

        tk.Label(size_frame, text="Size pencil").pack(side=tk.LEFT)
        self.size_slider = tk.Scale(size_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=self.set_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side=tk.LEFT)

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, value):
        self.brush_size = int(value)

    def draw(self, event):
        x, y = event.x, event.y
        r = self.brush_size
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r,
            fill=self.color, outline=self.color
        )

    def clear_canvas(self):
        self.canvas.delete("all")





if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()