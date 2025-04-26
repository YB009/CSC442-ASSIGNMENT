##(c) Extends my program to have a python-based GUI
import tkinter as tk
from tkinter import messagebox
from app import calculate_real_size, get_db_connection

def calculate_and_store():
    try:
        username = username_entry.get()
        microscope_size = float(microscope_size_entry.get())
        magnification = float(magnification_entry.get())
        actual_size = calculate_real_size(microscope_size, magnification)
        actual_size_label.config(text=f"Actual size: {actual_size} μm")

        with get_db_connection() as conn:
            conn.execute("""
                INSERT INTO specimens (username, microscope_size, magnification, actual_size)
                VALUES (?, ?, ?, ?)
            """, (username, microscope_size, magnification, actual_size))
        
        messagebox.showinfo("Success", "Data stored successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

# Initialize GUI
root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Microscope size (μm):").pack()
microscope_size_entry = tk.Entry(root)
microscope_size_entry.pack()

tk.Label(root, text="Magnification:").pack()
magnification_entry = tk.Entry(root)
magnification_entry.pack()

calculate_button = tk.Button(root, text="Calculate and Store", command=calculate_and_store)
calculate_button.pack()

actual_size_label = tk.Label(root, text="Actual size: ")
actual_size_label.pack()

root.mainloop()