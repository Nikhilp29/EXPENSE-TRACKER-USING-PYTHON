import tkinter
from tkinter import messagebox
import os
def login():
    username = "admin"
    password = "1234"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        os.system('newexpense1.py')
       
    else:
        messagebox.showerror(title="Error", message="Invalid login.") 
       
window = tkinter.Tk()
frame = tkinter.Frame(bg='#80afd6')
login_label = tkinter.Label(frame, text="Login Page", bg='#000000', fg="#FFFFFF", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#000000', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#000000', fg="#FFFFFF", font=("Arial", 16, 'bold'))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="#000000", fg="#FFFFFF", font=("Arial", 16), command=login)
login_label.grid(row=1, column=1, columnspan=2, sticky="news", pady=40)
username_label.grid(row=2, column=1)
username_entry.grid(row=2, column=2, pady=20)
password_label.grid(row=3, column=1)
password_entry.grid(row=3, column=2, pady=20)
login_button.grid(row=4, column=1, columnspan=2, pady=30)
window.title("EXPENSE TRACKER LOGIN PAGE")
window.geometry('750x550')
window.configure(bg='#80afd6')
frame.pack()
window.mainloop()
