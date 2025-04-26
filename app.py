from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask import flash

app = Flask(__name__)

# Database configuration
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specimens.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS specimens (
                username TEXT,
                microscope_size REAL,
                magnification REAL,
                actual_size REAL
            )
        """)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            username = request.form["username"]
            microscope_size = float(request.form["microscope_size"])
            magnification = float(request.form["magnification"])
            actual_size = microscope_size / magnification

            with get_db_connection() as conn:
                conn.execute("""
                    INSERT INTO specimens (username, microscope_size, magnification, actual_size)
                    VALUES (?, ?, ?, ?)
                """, (username, microscope_size, magnification, actual_size))
            
            flash("Specimen data stored successfully!", "success")
            return redirect(url_for("index"))
            
        except ValueError:
            flash("Invalid input. Please enter valid numbers.", "error")
            return redirect(url_for("index"))

    with get_db_connection() as conn:
        specimens = conn.execute("SELECT * FROM specimens").fetchall()
    
    return render_template("index.html", specimens=specimens)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)