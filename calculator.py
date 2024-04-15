from tkinter import *
from tkinter import messagebox

# Functions
def calculate():
    try:
        result = eval(entryText.get())
        entryText.set(result)
    except:
        e.delete(0, END)
        messagebox.showerror("Error", "An error occurred.")

# create the window
root = Tk()
root.title("Calculator")
root.config(bg="lightblue")
root.geometry("300x300")
root.resizable(0, 0)
img = Image('photo', file='calculator.png')
root.call('wm', 'iconphoto', root._w, img)

# Frame
frame = Frame(root)
frame.pack(pady=10, anchor=S)

# Widgets
entryText = StringVar()
e = Entry(frame, font=("Arial", 15), textvariable=entryText)
e.grid(row=0, column=0, columnspan=4)

b0 = Button(frame, text="0", width=11, height=2, command=lambda: e.insert(END,"0"))
b1 = Button(frame, text="1", width=5, height=2, command=lambda: e.insert(END,"1"))
b2 = Button(frame, text="2", width=5, height=2, command=lambda: e.insert(END,"2"))
b3 = Button(frame, text="3", width=5, height=2, command=lambda: e.insert(END,"3"))
b4 = Button(frame, text="4", width=5, height=2, command=lambda: e.insert(END,"4"))
b5 = Button(frame, text="5", width=5, height=2, command=lambda: e.insert(END,"5"))
b6 = Button(frame, text="6", width=5, height=2, command=lambda: e.insert(END,"6"))
b7 = Button(frame, text="7", width=5, height=2, command=lambda: e.insert(END,"7"))
b8 = Button(frame, text="8", width=5, height=2, command=lambda: e.insert(END,"8"))
b9 = Button(frame, text="9", width=5, height=2, command=lambda: e.insert(END,"9"))

bDiv = Button(frame, text="\U000000F7", width=5, height=2, command=lambda: e.insert(END,"/"))
bMul = Button(frame, text="\U000000D7", width=5, height=2, command=lambda: e.insert(END,"*"))
bPlus = Button(frame, text="+", width=5, height=2, command=lambda: e.insert(END,"+"))
bSub = Button(frame, text="-", width=5, height=2, command=lambda: e.insert(END,"-"))
bEqu = Button(frame, text="=", width=5, height=2, command=calculate)
bFlo = Button(frame, text=".", width=5, height=2, command=lambda: e.insert(END,"."))
bClear = Button(frame, text="AC", width=16, height=2, command=lambda: e.delete(0, END))


b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bDiv.grid(row=1, column=3)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bMul.grid(row=2, column=3)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
bSub.grid(row=3, column=3)

b0.grid(row=4, column=0, columnspan=2)
bPlus.grid(row=4, column=2)
bEqu.grid(row=4, column=3)

bFlo.grid(row=5, column=0)
bClear.grid(row=5, column=1, columnspan=3)

root.mainloop()
