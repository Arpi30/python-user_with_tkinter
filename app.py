from tkinter import *
from tkinter import ttk
from db_manager import *

win = Tk()
win.geometry("1020x640")
win.title("Users")
win.resizable(False, False)

db_create()

Label(win, text="Name", font="Helvetica 12 bold").grid(row=0, column=0)
name = Entry(win, font="Helvetica 20 bold")
name.grid(row=0, column=1, padx=5, pady=5)

Label(win, text="Age", font="Helvetica 12 bold").grid(row=1, column=0)
age = Entry(win, font="Helvetica 20 bold")
age.grid(row=1, column=1, padx=5, pady=5)

Label(win, text="Gender", font="Helvetica 12 bold").grid(row=2, column=0)
gender = StringVar(win)
gender.set("Select you gender")
select_gender = OptionMenu(win, gender, "male", "female")
select_gender.grid(row=2, column=1, padx=5, pady=5)

Label(win, text="Score", font="Helvetica 12 bold").grid(row=3, column=0)
score = Entry(win, font="Helvetica 20 bold")
score.grid(row=3, column=1, padx=5, pady=5)

insert_button = Button(win, text="Insert data",
                       font="Helvetica 12 bold", command=lambda: create_user(name, age, gender, score))
insert_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

cols = ("id", "Name", "Age", "Gender", "Score")
table = ttk.Treeview(win, columns=cols, show="headings")
for col in cols:
    table.heading(col, text=col)
table.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

query_button = Button(win, text="Query data",
                      font="Helvetica 12 bold", command=lambda: db_query(table))
query_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

export_csv = Button(win, text="Export to csv",
                    font="Helvetica 12 bold", command=export_to_csv)
export_csv.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

win.mainloop()
db_close()
