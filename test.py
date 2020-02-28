import sqlite3

connection = sqlite3.connect('data.db')

cursor =  connection.cursor()

create_table = "CREATE TABLE users(id int, username text, password text)"
cursor.execute(create_table)

user = (1, "john", "doe")
insert_table = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_table, user)

users = [
    (2, "mary", "jane"),
    (3, "peter", "parker")
]
cursor.executemany(insert_table, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()