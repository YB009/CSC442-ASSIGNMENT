## (b) This file  Extends my program to have a database that stores username, specimen size, and actual size.
from app import calculate_real_size, initialize_database, get_db_connection

def store_specimen(username, microscope_size, magnification, actual_size):
    with get_db_connection() as conn:
        conn.execute("""
            INSERT INTO specimens (username, microscope_size, magnification, actual_size)
            VALUES (?, ?, ?, ?)
        """, (username, microscope_size, magnification, actual_size))

def main():
    initialize_database()
    
    username = input("Enter your username: ")
    microscope_size = float(input("Enter the size under the microscope (μm): "))
    magnification = float(input("Enter the magnification: "))
    actual_size = calculate_real_size(microscope_size, magnification)
    
    store_specimen(username, microscope_size, magnification, actual_size)
    print(f"Real-life size: {actual_size} μm (stored in database)")

if __name__ == "__main__":
    main()