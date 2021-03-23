import sqlite3
from headers import get_headers

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# id INTEGER PRIMARY KEY enables us to have a auto incrementing id. 
# create_table_stocks = "CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, symbol text, avgprice float)"
create_table_stocks = "CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, symbol text, avgprice float, previousclose float)"
create_table_stocks = "CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, symbol text, avgprice float, previousclose float)"
headers_retreived = get_headers()
create_table_stocks = "CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, "
for ctr,header in enumerate(headers_retreived):
    if ctr == len(headers_retreived)- 1:
        create_table_stocks += "{} text )".format(header )
    else:
        create_table_stocks += "{} text, ".format(header )
    print(header, end = " ")

print("*"*40)
print(create_table_stocks)
print("*"*40)
cursor.execute(create_table_stocks)

# # create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# # cursor.execute(create_table_items)


connection.commit()
connection.close()
