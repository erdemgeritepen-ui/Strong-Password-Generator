import random
import tkinter as tk
down_keys = "abcdefghijklmnoprstqwxuvyz"
up_keys = "ABCDEFGHİJKLMNOPRSTQWXUVYZ"
numbers = "0123456789"
secret = "!?*@&%$#£"
all_chars = down_keys + up_keys + numbers + secret
character = 8
def new_password():
    key = "".join(random.choice(all_chars) for _ in range(character))
    Ktext.config(text=key)
screen = tk.Tk()
screen.geometry("400x300")
Ktext = tk.Label(text=("Press The Button To New Password"), font=("Arial", 16))
Ktext.pack(pady=50)
ChangeBttn = tk.Button(text=("Press"), font=("Arial", 16),command=new_password)
ChangeBttn.pack(pady=20)
def copyy():
    screen.clipboard_clear()
    screen.clipboard_append(Ktext.cget("text"))
copybutnn = tk.Button(text=("Copy"), font=("Arial", 16),command=copyy)
copybutnn.pack(pady=20)
screen.mainloop()
