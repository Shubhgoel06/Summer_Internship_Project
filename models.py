from datetime import datetime

class Flight:
    def __init__(self, flight_number, source, destination, departure_time, arrival_time, gate, status="On Time"):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M:%S")
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d %H:%M:%S")
        self.gate = gate
        self.status = status

class Passenger:
    def __init__(self, name, passport_number, flight_id, seat_number, check_in_status="Not Checked In", baggage_info=""):
        self.name = name
        self.passport_number = passport_number
        self.flight_id = flight_id
        self.seat_number = seat_number
        self.check_in_status = check_in_status
        self.baggage_info = baggage_info

class Staff:
    def __init__(self, name, role, shift_timing, assigned_flight=None):
        self.name = name
        self.role = role
        self.shift_timing = shift_timing
        self.assigned_flight = assigned_flight

class Gate:
    def __init__(self, gate_id, flight_id=None, availability_status="Available"):
        self.gate_id = gate_id
        self.flight_id = flight_id
        self.availability_status = availability_status

class Baggage:
    def __init__(self, passenger_id, flight_id, weight, status):
        self.passenger_id = passenger_id
        self.flight_id = flight_id
        self.weight = weight
        self.status = status


