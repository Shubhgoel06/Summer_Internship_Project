import tkinter as tk
from tkinter import messagebox
from database import add_flight, get_flights, add_passenger, get_passengers, add_staff, get_staff, add_gate, get_gates
from models import Flight, Passenger, Staff, Gate

def add_flight_gui():
    def save_flight():
        flight_number = entry_flight_number.get()
        source = entry_source.get()
        destination = entry_destination.get()
        departure_time = entry_departure_time.get()
        arrival_time = entry_arrival_time.get()
        gate = entry_gate.get()
        status = entry_status.get()

        if flight_number and source and destination and departure_time and arrival_time and gate and status:
            flight = Flight(flight_number, source, destination, departure_time, arrival_time, gate, status)
            add_flight(flight)
            messagebox.showinfo("Success", "Flight added successfully!")
            add_flight_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_flight_window = tk.Toplevel()
    add_flight_window.title("Add Flight")
    add_flight_window.configure(bg="#f0f8ff")

    tk.Label(add_flight_window, text="Flight Number:", bg="#f0f8ff").pack(pady=5)
    entry_flight_number = tk.Entry(add_flight_window)
    entry_flight_number.pack(pady=5)

    tk.Label(add_flight_window, text="Source:", bg="#f0f8ff").pack(pady=5)
    entry_source = tk.Entry(add_flight_window)
    entry_source.pack(pady=5)

    tk.Label(add_flight_window, text="Destination:", bg="#f0f8ff").pack(pady=5)
    entry_destination = tk.Entry(add_flight_window)
    entry_destination.pack(pady=5)

    tk.Label(add_flight_window, text="Departure Time:", bg="#f0f8ff").pack(pady=5)
    entry_departure_time = tk.Entry(add_flight_window)
    entry_departure_time.pack(pady=5)

    tk.Label(add_flight_window, text="Arrival Time:", bg="#f0f8ff").pack(pady=5)
    entry_arrival_time = tk.Entry(add_flight_window)
    entry_arrival_time.pack(pady=5)

    tk.Label(add_flight_window, text="Gate:", bg="#f0f8ff").pack(pady=5)
    entry_gate = tk.Entry(add_flight_window)
    entry_gate.pack(pady=5)

    tk.Label(add_flight_window, text="Status:", bg="#f0f8ff").pack(pady=5)
    entry_status = tk.Entry(add_flight_window)
    entry_status.pack(pady=5)

    tk.Button(add_flight_window, text="Save Flight", command=save_flight, bg="#4caf50", fg="white").pack(pady=10)

def view_flights_gui():
    flights = get_flights()

    view_flights_window = tk.Toplevel()
    view_flights_window.title("View Flights")
    view_flights_window.configure(bg="#f0f8ff")

    tk.Label(view_flights_window, text="Flights Information", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)
    
    for flight in flights:
        flight_info = f"Flight Number: {flight[0]}, Source: {flight[1]}, Destination: {flight[2]}, Departure: {flight[3]}, Arrival: {flight[4]}, Gate: {flight[5]}, Status: {flight[6]}"
        tk.Label(view_flights_window, text=flight_info, bg="#f0f8ff").pack(pady=5)

def add_passenger_gui():
    def save_passenger():
        name = entry_name.get()
        passport_number = entry_passport_number.get()
        flight_id = entry_flight_id.get()
        seat_number = entry_seat_number.get()
        check_in_status = entry_check_in_status.get()
        baggage_info = entry_baggage_info.get()

        if name and passport_number and flight_id and seat_number and check_in_status and baggage_info:
            passenger = Passenger(name, passport_number, flight_id, seat_number, check_in_status, baggage_info)
            add_passenger(passenger)
            messagebox.showinfo("Success", "Passenger added successfully!")
            add_passenger_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_passenger_window = tk.Toplevel()
    add_passenger_window.title("Add Passenger")
    add_passenger_window.configure(bg="#f0f8ff")

    tk.Label(add_passenger_window, text="Name:", bg="#f0f8ff").pack(pady=5)
    entry_name = tk.Entry(add_passenger_window)
    entry_name.pack(pady=5)

    tk.Label(add_passenger_window, text="Passport Number:", bg="#f0f8ff").pack(pady=5)
    entry_passport_number = tk.Entry(add_passenger_window)
    entry_passport_number.pack(pady=5)

    tk.Label(add_passenger_window, text="Flight ID:", bg="#f0f8ff").pack(pady=5)
    entry_flight_id = tk.Entry(add_passenger_window)
    entry_flight_id.pack(pady=5)

    tk.Label(add_passenger_window, text="Seat Number:", bg="#f0f8ff").pack(pady=5)
    entry_seat_number = tk.Entry(add_passenger_window)
    entry_seat_number.pack(pady=5)

    tk.Label(add_passenger_window, text="Check-in Status:", bg="#f0f8ff").pack(pady=5)
    entry_check_in_status = tk.Entry(add_passenger_window)
    entry_check_in_status.pack(pady=5)

    tk.Label(add_passenger_window, text="Baggage Info:", bg="#f0f8ff").pack(pady=5)
    entry_baggage_info = tk.Entry(add_passenger_window)
    entry_baggage_info.pack(pady=5)

    tk.Button(add_passenger_window, text="Save Passenger", command=save_passenger, bg="#4caf50", fg="white").pack(pady=10)

def view_passengers_gui():
    passengers = get_passengers()

    view_passengers_window = tk.Toplevel()
    view_passengers_window.title("View Passengers")
    view_passengers_window.configure(bg="#f0f8ff")

    tk.Label(view_passengers_window, text="Passengers Information", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)
    
    for passenger in passengers:
        passenger_info = f"Name: {passenger[0]}, Passport: {passenger[1]}, Flight ID: {passenger[2]}, Seat: {passenger[3]}, Check-in Status: {passenger[4]}, Baggage Info: {passenger[5]}"
        tk.Label(view_passengers_window, text=passenger_info, bg="#f0f8ff").pack(pady=5)

def add_staff_gui():
    def save_staff():
        name = entry_name.get()
        role = entry_role.get()
        shift_timing = entry_shift_timing.get()
        assigned_flight = entry_assigned_flight.get()

        if name and role and shift_timing and assigned_flight:
            staff = Staff(name, role, shift_timing, assigned_flight)
            add_staff(staff)
            messagebox.showinfo("Success", "Staff added successfully!")
            add_staff_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_staff_window = tk.Toplevel()
    add_staff_window.title("Add Staff")
    add_staff_window.configure(bg="#f0f8ff")

    tk.Label(add_staff_window, text="Name:", bg="#f0f8ff").pack(pady=5)
    entry_name = tk.Entry(add_staff_window)
    entry_name.pack(pady=5)

    tk.Label(add_staff_window, text="Role:", bg="#f0f8ff").pack(pady=5)
    entry_role = tk.Entry(add_staff_window)
    entry_role.pack(pady=5)

    tk.Label(add_staff_window, text="Shift Timing:", bg="#f0f8ff").pack(pady=5)
    entry_shift_timing = tk.Entry(add_staff_window)
    entry_shift_timing.pack(pady=5)

    tk.Label(add_staff_window, text="Assigned Flight:", bg="#f0f8ff").pack(pady=5)
    entry_assigned_flight = tk.Entry(add_staff_window)
    entry_assigned_flight.pack(pady=5)

    tk.Button(add_staff_window, text="Save Staff", command=save_staff, bg="#4caf50", fg="white").pack(pady=10)

def view_staff_gui():
    staff_list = get_staff()

    view_staff_window = tk.Toplevel()
    view_staff_window.title("View Staff")
    view_staff_window.configure(bg="#f0f8ff")

    tk.Label(view_staff_window, text="Staff Information", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)
    
    for staff in staff_list:
        staff_info = f"Name: {staff[0]}, Role: {staff[1]}, Shift Timing: {staff[2]}, Assigned Flight: {staff[3]}"
        tk.Label(view_staff_window, text=staff_info, bg="#f0f8ff").pack(pady=5)

def add_gate_gui():
    def save_gate():
        gate_id = entry_gate_id.get()
        flight_id = entry_flight_id.get()
        availability_status = entry_availability_status.get()

        if gate_id and flight_id and availability_status:
            gate = Gate(gate_id, flight_id, availability_status)
            add_gate(gate)
            messagebox.showinfo("Success", "Gate added successfully!")
            add_gate_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    add_gate_window = tk.Toplevel()
    add_gate_window.title("Add Gate")
    add_gate_window.configure(bg="#f0f8ff")

    tk.Label(add_gate_window, text="Gate ID:", bg="#f0f8ff").pack(pady=5)
    entry_gate_id = tk.Entry(add_gate_window)
    entry_gate_id.pack(pady=5)

    tk.Label(add_gate_window, text="Flight ID:", bg="#f0f8ff").pack(pady=5)
    entry_flight_id = tk.Entry(add_gate_window)
    entry_flight_id.pack(pady=5)

    tk.Label(add_gate_window, text="Availability Status:", bg="#f0f8ff").pack(pady=5)
    entry_availability_status = tk.Entry(add_gate_window)
    entry_availability_status.pack(pady=5)

    tk.Button(add_gate_window, text="Save Gate", command=save_gate, bg="#4caf50", fg="white").pack(pady=10)

def view_gates_gui():
    gates = get_gates()

    view_gates_window = tk.Toplevel()
    view_gates_window.title("View Gates")
    view_gates_window.configure(bg="#f0f8ff")

    tk.Label(view_gates_window, text="Gates Information", font=("Helvetica", 14), bg="#f0f8ff").pack(pady=10)
    
    for gate in gates:
        gate_info = f"Gate ID: {gate[0]}, Flight ID: {gate[1]}, Availability Status: {gate[2]}"
        tk.Label(view_gates_window, text=gate_info, bg="#f0f8ff").pack(pady=5)

def main_menu():
    root = tk.Tk()
    root.title("Airport Management System")
    root.configure(bg="#e0f7fa")

    tk.Label(root, text="Airport Management System", font=("Helvetica", 16), bg="#e0f7fa").pack(pady=10)

    tk.Button(root, text="Add Flight", command=add_flight_gui, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(root, text="View Flights", command=view_flights_gui, bg="#4caf50", fg="white").pack(pady=5)
    
    tk.Button(root, text="Add Passenger", command=add_passenger_gui, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(root, text="View Passengers", command=view_passengers_gui, bg="#4caf50", fg="white").pack(pady=5)
    
    tk.Button(root, text="Add Staff", command=add_staff_gui, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(root, text="View Staff", command=view_staff_gui, bg="#4caf50", fg="white").pack(pady=5)
    
    tk.Button(root, text="Add Gate", command=add_gate_gui, bg="#4caf50", fg="white").pack(pady=5)
    tk.Button(root, text="View Gates", command=view_gates_gui, bg="#4caf50", fg="white").pack(pady=5)

    tk.Button(root, text="Exit", command=root.quit, bg="#f44336", fg="white").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
