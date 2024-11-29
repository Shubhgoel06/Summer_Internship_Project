import sqlite3
from models import Flight, Passenger, Staff, Gate, Baggage

def add_flight(flight):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Flights (flight_number, source, destination, departure_time, arrival_time, gate, status)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                      (flight.flight_number, flight.source, flight.destination, flight.departure_time, flight.arrival_time, flight.gate, flight.status))

    conn.commit()
    conn.close()

def get_flights():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Flights')
    flights = cursor.fetchall()
    conn.close()
    return flights

def add_passenger(passenger):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute(''' INSERT INTO Passengers (name, passport_number, flight_id, seat_number, check_in_status, baggage_info)
                       VALUES(?,?,?,?,?,?)''',
                       (passenger.name, passenger.passport_number, passenger.flight_id, passenger.seat_number, passenger.check_in_status, passenger.baggage_info))
    conn.commit()
    conn.close()

def get_passengers():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Passengers')
    passengers = cursor.fetchall()
    conn.close()
    return passengers

def add_staff(staff):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Staff (name, role, shift_timing, assigned_flight)
                      VALUES(?,?,?,?)''',
                      (staff.name, staff.role, staff.shift_timing, staff.assigned_flight))
    conn.commit()
    conn.close()

def get_staff():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Staff')
    staff = cursor.fetchall()
    conn.close()
    return staff

def add_gate(gate):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Gates (gate_id, flight_id, availability_status)
                    VALUES(?,?,?)''',
                   (gate.gate_id, gate.flight_id, gate.availability_status))
    conn.commit()
    conn.close()

def get_gates():
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Gates')
    gates = cursor.fetchall()
    conn.close()
    return gates

def add_baggage(baggage):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Baggage (passenger_id, flight_id, status)
                      VALUES (?, ?, ?)''',
                   (baggage.passenger_id, baggage.flight_id, baggage.status))
    
    baggage_id = cursor.lastrowid  # Get the ID of the last inserted row

    conn.commit()
    conn.close()

    return baggage_id

def update_baggage_status(baggage_id, status):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE Baggage SET status = ?, last_updated = CURRENT_TIMESTAMP WHERE baggage_id = ?''',
                   (status, baggage_id))
    conn.commit()
    conn.close()

def get_baggage_status(baggage_id):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT status, last_updated FROM Baggage WHERE baggage_id = ?', (baggage_id,))
    status = cursor.fetchone()
    conn.close()
    return status

def get_baggage_by_passenger(passport_number):
    conn = sqlite3.connect('airport.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Baggage WHERE passenger_id = ?', (passport_number,))
    baggage = cursor.fetchall()
    conn.close()
    return baggage
