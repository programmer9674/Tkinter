from tkinter import *
from tkinter import messagebox
import random


class GuessNumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess Number Game")
        self.root.geometry("400x300")
        self.root.config(bg="#BDFCC9")

        self.random_number = random.randint(10, 100)
        self.chance = 10

        self.label1 = Label(self.root, text="Guess a number between 10 and 100", background="#BDFCC9")
        self.label1.pack(pady=10)

        self.label2 = Label(self.root, text=f"You have {self.chance} more chances.", background="#BDFCC9")
        self.label2.pack(pady=10)

        self.entry = Entry(self.root)
        self.entry.pack(pady=10)

        self.btn = Button(self.root, text="Check", command=self.check_number)
        self.btn.pack(pady=10)

        self.result = Label(self.root, text="", background="#BDFCC9")
        self.result.pack(pady=10)
    
    def check_number(self):
        try:
            n = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number")
            return
        
        self.entry.delete(0, END)
        if n < 10 or n > 100:
            messagebox.showwarning("Warning", "Out of range.")
        elif n == self.random_number:
            self.result.config(text="You Win")
            ans = messagebox.askyesno("Congratulation", "You win the game. Again?")
            if ans:
                self.restart()
            else:
                self.root.destroy()
            return
        elif n > self.random_number:
            self.result.config(text="Too High")
        else:
            self.result.config(text="Too Low")
        self.chance -= 1
        self.label2.config(text=f"You have {self.chance} more chances.")
        self.label2.update_idletasks()
        if self.chance == 0:
            ans = messagebox.askretrycancel("Ops", "You Lost the game. Again?")
            if ans:
                self.restart()
            else:
                self.root.destroy()
        
    def restart(self):
        # self.root.destroy()
        # root = Tk()
        # GuessNumber(root)
        # root.mainloop()
        self.random_number = random.randint(10, 100)
        self.chance = 10
        self.result.config(text="")
        self.label2.config(text=f"You have {self.chance} more chances.")

        

            


root = Tk()
GuessNumber(root)
root.mainloop()