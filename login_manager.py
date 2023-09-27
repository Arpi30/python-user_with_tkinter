import sqlite3
from app import *


conn = None
curs = None

def db_create_reg_table():
    global conn,curs
    conn = sqlite3.connect("users.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS registration (username TEXT, password TEXT)")

def registration(username_get, password_get, message):
    if not username_get.get() and not password_get.get():
        message.showerror(title="Registration error", message="Fields are mandatory")
        return
    curs.execute("INSERT INTO registration VALUES (?, ?)", (username_get.get(), password_get.get()))
    conn.commit()
    username_get.delete(0, 'end')
    password_get.delete(0, 'end')
    message.showinfo(title="registration", message="successfully registration! You can now log in! ")
    

def login(username_get, password_get, message_win, window):
    uname = username_get.get()
    password = password_get.get()

    curs.execute("SELECT * FROM registration WHERE username = ? AND password = ?", [(uname), (password)])
    datas = curs.fetchall()
    
    if  datas:
        message_win.showinfo(title="Login Successful!", message="You successfully logged in.")
        window.destroy()
        logged_in()
    else:
        message_win.showerror(title="Error", message="Invalid login.")
        username_get.delete(0, 'end')
        password_get.delete(0, 'end')
        




def close_reg_table():
    if conn and curs:
        conn.close()
        curs.close()
