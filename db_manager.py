import sqlite3

conn = None
curs = None


def db_create():
    global conn, curs
    conn = sqlite3.connect("users.db")
    curs = conn.cursor()

    curs.execute(
        "CREATE TABLE IF NOT EXISTS users (name Text, age INTEGER, gender TEXT, score REAL)")


def create_user(name, age, gender, score):
    if not name.get() or not age.get() or gender.get() == "Select you gender" or not score.get():
        print("Az osszes mezo kitoltese kotelezo")
        return
    curs.execute("INSERT INTO users VALUES (?,?,?,?)",
                 (name.get(), age.get(), gender.get(), score.get()))
    conn.commit()
    name.delete(0, 'end')
    age.delete(0, 'end')
    score.delete(0, 'end')


def db_query(table):
    curs.execute("SELECT * FROM users")
    datas = curs.fetchall()
    table.delete(*table.get_children())
    rowid = 1
    for data in datas:
        table.insert("", "end", values=(
            rowid, data[0], data[1], data[2], data[3]))
        rowid += 1


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
