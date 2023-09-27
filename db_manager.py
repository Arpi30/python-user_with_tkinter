import sqlite3
from tkinter import *
import random
from PIL import Image, ImageTk

conn = None
curs = None
img_photo = None


def db_create():
    global conn, curs
    conn = sqlite3.connect("users.db")
    curs = conn.cursor()
    curs.execute(
        "CREATE TABLE IF NOT EXISTS users (name Text, id INTEGER, age INTEGER, gender TEXT, score REAL, permission TEXT, login INTEGER)")


def create_user(name, age, gender, score, permission):
    rand_int = random.randint(1, 1000)
    login = 1
    if not name.get() or not age.get() or gender.get() == "Select you gender" or not score.get() or permission.get() == "Permission":
        print("All field is mandatory")
        return

    curs.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)",
                 (name.get(), rand_int, age.get(), gender.get(), score.get(), permission.get(), login))
    conn.commit()
    name.delete(0, 'end')
    age.delete(0, 'end')
    score.delete(0, 'end')


def search_user(search_id, table):
    if not search_id.get():
        print("Field is mandatory")

    curs.execute("SELECT * FROM users WHERE id = ?", (search_id.get(),))
    datas = curs.fetchall()
    table.delete(*table.get_children())
    table.insert("", "end", values=(datas[0]))
    search_id.delete(0, 'end')


def delete(table):
    # Get row id from treeview
    item = table.selection()
    if not item:
        print("Nincs kiválasztva elem a törléshez.")
        return

    selected_item_id = table.item(item, "values")[1]

    curs.execute("DELETE FROM users WHERE id = ?", (selected_item_id,))
    table.delete(item)
    conn.commit()


def imgShow(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    return photo


def db_query(table):
    global img_photo
    curs.execute("SELECT * FROM users ORDER BY name ASC")
    datas = curs.fetchall()
    table.delete(*table.get_children())
    img_photo = imgShow("logged.png")

    for data in datas:
        table.insert("", "end", values=(
            data[0], data[1], data[2], data[3], data[4], data[5], data[6]), image=img_photo)


def export_to_csv():
    # Adatok lekerese
    curs.execute("SELECT * FROM users")
    # Adatok elmentese
    datas = curs.fetchall()
    # Exportalas CSV file-ba
    with open("user.csv", "w", encoding="utf-8") as data:
        # write metodussal beallitjuk a csv header-jet. ;-vel valassza el majd a join metodussal hozzaadjuk a header ertekeit egy ilstben
        data.write(
            ";".join(["id", "name", "age", "gender", "score", "Permission"]))
        # at loopolunk a fetchelt listan
        data.write("\n")
        for d in datas:
            # szinten write metodussal hozzaadjuk a csv file-hoz a datas elemeit ami tuple. List comprehension-el at loopolunk a belso tuple-okon
            data.write(";".join(str(item) for item in d))
            # newline karakter
            data.write("\n")


def on_double_click(table, event, win):
    # Az identify_region metodus vissza adja a treeview-ban levo pont koordinatait ami egz string lesz, pl: heading, cell, tree, stb..
    region_clicked = table.identify_region(event.x, event.y)
    # ami nem cell tipusu mezo azt nem adja vissza
    if region_clicked not in ("cell"):
        return
    # vissza adja a treeview oszlopat
    column = table.identify_column(event.x)
    # Ezt a reszt nem ertem annyira, utana kell neznem!
    colum_index = int(column[1:]) - 1

    # vissza adja egy adott sor id-jat
    selected_id = table.focus()
    # vissza adja az adott sor elemeit egy dictben
    selected_values = table.item(selected_id)
    # vissza adja egy adott sor erteket egy tomben
    selected_text = selected_values.get('values')[colum_index]

    column_box = table.bbox(selected_id, column)

    entry_edit = Entry(win, width=column_box[2], text=selected_text)
    # Column index es item id, duppla kattintasra benne marad a cell erteke
    entry_edit.editing_column_index = colum_index
    entry_edit.editing_item_iid = selected_id
    entry_edit.insert(0, selected_text)
    entry_edit.select_range(0, END)
    entry_edit.focus()
    # eventek
    entry_edit.bind("<FocusOut>", lambda e: e.widget.destroy())
    entry_edit.bind("<Return>", lambda e,
                    table=table: on_entered_pressed(e, table))

    entry_edit.place(x=column_box[0] + 5, y=column_box[1] + 372,
                     w=column_box[2], h=column_box[3])


def on_entered_pressed(e, table):
    new_text = e.widget.get()
    selected_id = e.widget.editing_item_iid
    column_index = e.widget.editing_column_index
    column_name = table.heading(column_index)["text"]

    current_values = table.item(selected_id).get("values")
    current_values[column_index] = new_text
    table.item(selected_id, values=current_values)

    curs.execute(
        f'UPDATE users SET {column_name} = ? WHERE id = ?', (new_text, current_values[0],))
    conn.commit()
    e.widget.destroy()


def db_close():
    if conn and curs:
        curs.close()
        conn.close()
