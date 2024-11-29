import sqlite3

def create_tables():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Flights (
                      flight_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      flight_number TEXT,
                      source TEXT,
                      destination TEXT,
                      departure_time TEXT,
                      arrival_time TEXT,
                      gate TEXT,
                      status TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Passengers (
                      passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      passport_number TEXT,
                      flight_id INTEGER,
                      seat_number TEXT,
                      check_in_status TEXT,
                      baggage_info TEXT,
                      FOREIGN KEY(flight_id) REFERENCES Flights(flight_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Staff (
                      staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      role TEXT,
                      shift_timing TEXT,
                      assigned_flight INTEGER,
                      FOREIGN KEY(assigned_flight) REFERENCES Flights(flight_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Gates (
                      gate_id TEXT,
                      flight_id INTEGER,
                      availability_status TEXT,
                      FOREIGN KEY(flight_id) REFERENCES Flights(flight_id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Baggage (
    baggage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_id INTEGER,
    flight_id TEXT,
    status TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
