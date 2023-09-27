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

    curs.execute("SELECT * FROM registration WHERE username = ? AND password = ?", (username_get.get(), password_get.get(),))
    datas = curs.fetchall()
    print(datas)
    
    if datas and username_get.get() == datas[0][0] and password_get.get() == datas[0][1]:

        message_win.showinfo(title="Login Successful!", message="You successfully logged in.")
        window.destroy()
        logged_in()
    else:
        message_win.showerror(title="Error", message="Invalid login.")




def close_reg_table():
    if conn and curs:
        conn.close()
        curs.close()
