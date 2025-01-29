from tkinter import ttk, Tk, PhotoImage

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
image = PhotoImage(file="image.png")
ttk.Button(frm, image=image, padding=10, command=root.destroy).grid(column=1, row=0)
frm.image = image




root.mainloop()