import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS cart (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)")

# Insert sample data
cursor.execute("INSERT INTO products (name, price) VALUES ('Keyboard', 799)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Mouse', 499)")
cursor.execute("INSERT INTO cart (name, price) VALUES ('Keyboard', 799)")

conn.commit()
conn.close()
