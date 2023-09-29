import tkinter as tk
from tkinter import ttk
from db_manager import *
from tkinter import Menu



def logged_in():

    win = Tk()
    win.protocol("WM_DELETE_WINDOW",lambda:  db_close(win))
    win.geometry("1260x1000")
    mainmenu  = Menu(win)
    win.title("Users")
    win.resizable(False, False)
    style = ttk.Style()
    style.configure("Treeview", rowheight=35)
    style.configure("Treeview", rowheight=35)

    db_create()

    Label(win, text="Name", font="Helvetica 12 bold").grid(
        row=0, column=0, columnspan=1)
    name = Entry(win, font="Helvetica 20 bold")
    name.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

    Label(win, text="Age", font="Helvetica 12 bold").grid(
        row=1, column=0, columnspan=1)
    age = Entry(win, font="Helvetica 20 bold")
    age.grid(row=1, column=2, padx=5, pady=5, columnspan=2)

    Label(win, text="Gender", font="Helvetica 12 bold").grid(
        row=2, column=0, columnspan=1)
    gender = StringVar(win)
    gender.set("Select you gender")
    select_gender = OptionMenu(win, gender, "male", "female")
    select_gender.grid(row=2, column=2, padx=5, pady=5, columnspan=2)

    Label(win, text="Score", font="Helvetica 12 bold").grid(
        row=3, column=0, columnspan=1)
    score = Entry(win, font="Helvetica 20 bold")
    score.grid(row=3, column=2, padx=5, columnspan=2)

    Label(win, text="Permission", font="Helvetica 12 bold").grid(
        row=4, column=0, columnspan=1)
    permission = StringVar(win)
    permission.set("Permission")
    select_permission = OptionMenu(
        win, permission, "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    select_permission.grid(row=4, column=2, padx=5, pady=20, columnspan=2)

    Label(win, text="Search as ID", font="Helvetica 12 bold").grid(
        row=6, column=0, columnspan=1)
    search = Entry(win, font="Helvetica 20 bold")
    search.grid(row=6, column=1, columnspan=2)


    cols = ("Name", "id", "Age", "Gender", "Score", "Permission")
    table = ttk.Treeview(win, columns=cols)
    for col in cols:
        table.heading(col, text=col, anchor='center')
        table.column(col, anchor="center")
        table.column("#0", width=50, anchor="ne")
    table.grid(row=7, column=0, columnspan=5, padx=5, pady=5)

    table.bind("<Double-1>", lambda e: on_double_click(table, e, win))

    file_menu = Menu(mainmenu, tearoff=0)
    file_menu.config(bg="grey", fg='white')
    file_menu.add_command(label="Exit",font="Helvetica 8 bold", activeforeground="grey" , command=lambda: system_logout(win))
    file_menu.add_command(label="Export to cs", font="Helvetica 8 bold", activeforeground="grey", command=export_to_csv)
    file_menu.add_command(label="Import CSV", font="Helvetica 8 bold", activeforeground="grey", command=import_from_csv)

    mainmenu.add_cascade(label="Menu", menu=file_menu, font="Helvetica 10")  # Kapcsoljuk össze a "Menu" menüt a főmenüvel
    mainmenu.add_command(label="Query data", font="Helvetica 10", command=lambda: db_query(table))  # Kapcsoljuk össze a "Menu" menüt a főmenüvel
    win.config(menu=mainmenu)

    insert_button = Button(win, text="Insert data",
                        font="Helvetica 12 bold", command=lambda: create_user(name, age, gender, score, permission))
    insert_button.grid(row=5, column=0)

    button_del = Button(win, text="Delete", font="Helvetica 12 bold",
                        command=lambda: delete(table))
    button_del.grid(row=5, column=4, pady=20)

    button_search = Button(
        win, text="Search", font="Helvetica 12 bold", command=lambda: search_user(search, table))
    button_search.grid(row=6, column=4,  pady=10)

    win.mainloop()