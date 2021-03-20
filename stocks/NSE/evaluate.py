import sqlite3

def find_by_stock(name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
    query = "SELECT * FROM stocks WHERE symbol = ?"
    row = cursor.execute(query,(name,))
    row_fetched = row.fetchall()
    print(row_fetched)

while True:
    find_by_stock("PIIND")
    