from tkinter import *
import time

def display_datetime():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    time_label.config(text=f"{hour}:{minute}:{second} {time.strftime('%p')}")
    date_label.config(text=time.strftime("%x"))
    time_label.after(1000, display_datetime)

root = Tk()
root.geometry("300x100")
root.title('show date and time')
root.configure(bg="#3D59AB")

time_label = Label(root, text="", font=('arial', 25), bg="#3D59AB", fg='white')
time_label.pack(pady=10)

date_label = Label(root, text="", font=('arial', 15), bg="#3D59AB", fg='white')
date_label.pack(pady=10)
display_datetime()
root.mainloop()
