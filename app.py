import tkinter as tk
from tkinter import ttk
from db_manager import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("1260x1000")
win.title("Users")
win.resizable(False, False)
style = ttk.Style()
style.configure("Treeview", rowheight=35)
with Image.open("logged.png") as img_log:
    show_img = ImageTk.PhotoImage(img_log)


with Image.open("logged.png") as img_log:
    show_img = ImageTk.PhotoImage(img_log)

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
table.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

table.bind("<Double-1>", lambda e: on_double_click(table, e, win))

insert_button = Button(win, text="Insert data",
                       font="Helvetica 12 bold", command=lambda: create_user(name, age, gender, score, permission))
insert_button.grid(row=5, column=0)

query_button = Button(win, text="Query data",
                      font="Helvetica 12 bold", command=lambda: db_query(table))
query_button.grid(row=5, column=1)

export_csv = Button(win, text="Export to csv",
                    font="Helvetica 12 bold", command=export_to_csv)
export_csv.grid(row=5, column=2)

button_del = Button(win, text="Delete", font="Helvetica 12 bold",
                    command=lambda: delete(table))
button_del.grid(row=5, column=3, pady=20)

button_search = Button(
    win, text="Search", font="Helvetica 12 bold", command=lambda: search_user(search, table))
button_search.grid(row=6, column=3, columnspan=2, pady=10)

win.mainloop()
db_close()
