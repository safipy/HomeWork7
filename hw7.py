import sqlite3

db = sqlite3.connect('table.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
name text,
surname text,
hobby text,
year integer,
points integer
)''')


c.execute("INSERT INTO user VALUES ( 'Данияр','Жыргалбек', 'football', 2002, 10)")
c.execute("INSERT INTO user VALUES ( 'Назира', 'Абдиллаева', 'football', 2001, 10)")
c.execute("INSERT INTO user VALUES ( 'Абдула', 'Манаров','basketball', 2001, 9)")
c.execute("INSERT INTO user VALUES ( 'Адилет', 'Женишбеков', 'football', 2000, 10)")
c.execute("INSERT INTO user VALUES ( 'Сергей', 'Беляев', 'basketball', 1993, 5)")
c.execute("INSERT INTO user VALUES ( 'Алимбек', 'Акеров', 'valebol', 2004, 5)")
c.execute("INSERT INTO user VALUES ( 'Максим', 'Евтушенко', 'valebol', 1990, 10)")
c.execute("INSERT INTO user VALUES ( 'Арзыбек', 'Абдырахманов', 'basketball', 1999, 10)")
c.execute("INSERT INTO user VALUES ( 'Элдияр', 'Нурали', 'valebol',  2002, 10)")
c.execute("INSERT INTO user VALUES ( 'Бектур', 'Рысбаев', 'football', 2001, 10)")
c.execute("SELECT rowid FROM user")

c.execute("UPDATE user SET name = 'genius' WHERE points = 10")
c.execute("SELECT rowid, surname, name FROM user ")

items = c.fetchall()

print(items)

c.execute("SELECT rowid, name FROM user WHERE name = 'genius' ")
c.execute("DELETE FROM user WHERE rowid % 2 = 0")
print(c.fetchall())

db.commit()
db.close()