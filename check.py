import sqlite3
def check_table_structure():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Gates);")
    print(cursor.fetchall())
    conn.close()

check_table_structure()  # Call this function to see the table structure
