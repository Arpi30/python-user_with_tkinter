import sqlite3
from tkinter import *
conn = None
curs = None


def db_create():
    global conn, curs
    conn = sqlite3.connect("users.db")
    curs = conn.cursor()
    curs.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER, name Text, age INTEGER, gender TEXT, score REAL)")


def create_user(id, name, age, gender, score):
    if not name.get() or not age.get() or gender.get() == "Select you gender" or not score.get():
        print("Az osszes mezo kitoltese kotelezo")
        return

    curs.execute("INSERT INTO users VALUES (?,?,?,?,?)",
                 (id, name.get(), age.get(), gender.get(), score.get()))
    conn.commit()
    name.delete(0, 'end')
    age.delete(0, 'end')
    score.delete(0, 'end')


def delete(table):
    # Get row id from treeview
    item = table.selection()
    if not item:
        print("Nincs kiválasztva elem a törléshez.")
        return

    selected_item_id = table.item(item, "values")[0]

    curs.execute("DELETE FROM users WHERE id = ?", (selected_item_id,))
    table.delete(item)
    conn.commit()


def db_query(table):
    curs.execute("SELECT * FROM users")
    datas = curs.fetchall()
    table.delete(*table.get_children())

    for data in datas:
        table.insert("", "end", values=(
            data[0], data[1], data[2], data[3], data[4]))


def export_to_csv():
    # Adatok lekerese
    curs.execute("SELECT * FROM users")
    # Adatok elmentese
    datas = curs.fetchall()
    # Exportalas CSV file-ba
    with open("user.csv", "w", encoding="utf-8") as data:
        # write metodussal beallitjuk a csv header-jet. ;-vel valassza el majd a join metodussal hozzaadjuk a header ertekeit egy ilstben
        data.write(";".join(["name", "age", "gender", "score"]))
        # at loopolunk a fetchelt listan
        data.write("\n")
        for d in datas:
            # szinten write metodussal hozzaadjuk a csv file-hoz a datas elemeit ami tuple. List comprehension-el at loopolunk a belso tuple-okon
            data.write(";".join(str(item) for item in d))
            # newline karakter
            data.write("\n")


def db_close():
    if conn and curs:
        curs.close()
        conn.close()
