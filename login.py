from tkinter import ttk
from tkinter import messagebox
from login_manager import *
from app import *


window = Tk()
window.title("Login Page using Python")
window.geometry('750x550')
window.resizable(False, False)

db_create_reg_table()

frame = Frame()
login_label = Label(frame, text="FirstEmp", font=("Arial", 30))
username_label = Label(frame, text="Username", font=("Arial", 16, 'bold'))
password_label = Label(frame, text="Password", font=("Arial", 16, 'bold'))

username_entry = Entry(frame, font=("Arial", 16))
password_entry = Entry(frame, show="*", font=("Arial", 16))

login_button = Button(frame, text="Login", font=("Arial", 16), command=lambda: login(username_entry, password_entry, messagebox, window))
reg_button = Button(frame, text="Registration", font=("Arial", 16), command=lambda: registration(username_entry, password_entry, messagebox))

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, pady=30)
reg_button.grid(row=3, column=1, pady=30)

frame.pack()
window.mainloop()
close_reg_table()