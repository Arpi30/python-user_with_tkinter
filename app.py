from tkinter import *
from tkinter import ttk
from db_manager import *
import random

rand_int = random.randint(1, 1000)
win = Tk()
win.geometry("1020x640")
win.title("Users")
win.resizable(False, False)

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
score.grid(row=3, column=2, padx=5, pady=20, columnspan=2)

Label(win, text="Search as ID", font="Helvetica 12 bold").grid(
    row=5, column=0, columnspan=1)
search = Entry(win, font="Helvetica 20 bold")
search.grid(row=5, column=1, columnspan=2)


cols = ("id", "Name", "Age", "Gender", "Score")
table = ttk.Treeview(win, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col, anchor='center')
    table.column(col, anchor="center")
table.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

insert_button = Button(win, text="Insert data",
                       font="Helvetica 12 bold", command=lambda: create_user(rand_int, name, age, gender, score))
insert_button.grid(row=4, column=0)

query_button = Button(win, text="Query data",
                      font="Helvetica 12 bold", command=lambda: db_query(table))
query_button.grid(row=4, column=1)

export_csv = Button(win, text="Export to csv",
                    font="Helvetica 12 bold", command=export_to_csv)
export_csv.grid(row=4, column=2)

button_del = Button(win, text="Delete", font="Helvetica 12 bold",
                    command=lambda: delete(table))
button_del.grid(row=4, column=3, pady=20)

button_search = Button(
    win, text="Search", font="Helvetica 12 bold", command=lambda: search_user(search, table))
button_search.grid(row=5, column=3, columnspan=2, pady=10)

win.mainloop()
db_close()
