from tkinter import *
from tkinter.colorchooser import askcolor


def draw(event):
    x, y = event.x, event.y
    xn, yn = x + pen_size, y + pen_size
    canvas.create_oval((x, y, xn, yn), fill=pen_color, outline=pen_color)

    # canvas.create_line((x, y, xn, yn))
pen_size = 5


def change_pen_size(value):
    global pen_size
    pen_size = value
    # print(value, p.get())


def change_bg_color():
    color = askcolor()[1]
    canvas.config(bg=color)


pen_color = "black"


def change_pen_color():
    global pen_color
    pen_color = askcolor()[1]


def clear():
    canvas.delete("all")
    canvas.config(bg="white")


root = Tk()
root.title("Tkinter - Paint App")
root.geometry("530x600")
root.resizable(False, False)

canvas = Canvas(root, width=500, height=500, highlightbackground="black")
canvas.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

Label(root, text="Pen Size: ").grid(row=1, column=0)
options = range(1, 51)
p = StringVar()
p.set(pen_size)

change_pen_size_btn = OptionMenu(root, p, *options, command=change_pen_size)
change_pen_size_btn.grid(row=1, column=1)

change_bg_color_btn = Button(
    root, text="Change Background Color", command=change_bg_color)
change_bg_color_btn.grid(row=1, column=2)

change_pen_color_btn = Button(
    root, text="Change Pen Color", command=change_pen_color)
change_pen_color_btn.grid(row=1, column=3)

clear_btn = Button(root, text="🧹", command clear)
clear_btn.grid(row=1, column=4)

root.bind("<B1-Motion>", draw)

root.mainloop()
