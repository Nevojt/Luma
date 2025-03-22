from tkinter import *
import random

root = Tk()
root.title("Love calculator!!!!")
root.geometry("400x240")

def calculate_love():
    # st = "Help me, my friend!!!"    #"0123456789"
    # digit = 4
    # temp = "".join(random.sample(st, digit))
    temp = str(random.randint(0, 100))
    result.config(text=temp + "%")


heading = Label(root, text="Love Calculator")
heading.pack()

slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()


slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
            width=7, command=calculate_love)
bt.pack()

result = Label(root, text="Love percent ")
result.pack()





root.mainloop()