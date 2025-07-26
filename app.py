from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    return render_template("index.html", products=products)

@app.route("/cart")
def cart():
    db = get_db()
    items = db.execute("SELECT * FROM cart").fetchall()
    return render_template("cart.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
