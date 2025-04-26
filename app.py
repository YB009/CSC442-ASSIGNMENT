from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), "specimens.db")

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    
    # Create table if it doesn't exist
    conn.execute("""
        CREATE TABLE IF NOT EXISTS specimens (
            username TEXT,
            microscope_size REAL,
            magnification REAL,
            actual_size REAL
        )
    """)
    conn.commit()
    
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        microscope_size = float(request.form["microscope_size"])
        magnification = float(request.form["magnification"])
        actual_size = microscope_size / magnification

        conn = get_db()
        conn.execute("""
            INSERT INTO specimens VALUES (?, ?, ?, ?)
        """, (username, microscope_size, magnification, actual_size))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn = get_db()
    specimens = conn.execute("SELECT * FROM specimens").fetchall()
    conn.close()
    return render_template("index.html", specimens=specimens)

if __name__ == "__main__":
    with app.app_context():
        get_db()  # Initialize database
    app.run(debug=True)