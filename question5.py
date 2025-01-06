import heapq
from datetime import datetime

class Appointment:
    def __init__(self, patient_name, appointment_time, priority):
        self.patient_name = patient_name
        self.appointment_time = appointment_time  
        self.priority = priority  

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.appointment_time < other.appointment_time
        return self.priority < other.priority

    def __repr__(self):
           return f"Patient: {self.patient_name}, Time: {self.appointment_time.strftime('%Y-%m-%d %H:%M:%S')}, Priority: {self.priority}"

class AppointmentHeap:
    def __init__(self):
        self.heap = []

    def add_appointment(self, appointment):
        heapq.heappush(self.heap, appointment)

    def pop_appointment(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek_next_appointment(self):
        if self.heap:
            return self.heap[0]
        return None

    def view_appointments(self):
        return sorted(self.heap)

    def get_all_appointments(self):
        return self.heap

# Example 
if __name__ == "__main__":
    appointment_heap = AppointmentHeap()

    appointment1 = Appointment("naomi", datetime(2024, 12, 22, 14, 30), 2) 
    appointment2 = Appointment("lambery", datetime(2024, 12, 22, 9, 0), 3)
    appointment3 = Appointment("kalisa", datetime(2024, 12, 23, 10, 0), 1)
    appointment4 = Appointment("kamanzi", datetime(2024, 12, 22, 13, 30), 2)

    appointment_heap.add_appointment(appointment1)
    appointment_heap.add_appointment(appointment2)
    appointment_heap.add_appointment(appointment3)
    appointment_heap.add_appointment(appointment4)

    print("All Appointments (sorted by priority and time):")
    for app in appointment_heap.view_appointments():
        print(app)

    print("\nNext appointment to process (highest priority):")
    next_appointment = appointment_heap.pop_appointment()
    print(next_appointment)

    print("\nNext appointment to process (after popping one):")
    peek_appointment = appointment_heap.peek_next_appointment()
    print(peek_appointment)

    print("\nRemaining appointments:")
    while appointment_heap.get_all_appointments():
        print(appointment_heap.pop_appointment())
    
    print("\nAdding new appointments dynamically:")

    appointment5 = Appointment("fabrice", datetime(2024, 12, 23, 11, 0), 1)
    appointment6 = Appointment("fred", datetime(2024, 12, 22, 16, 0), 2)

    appointment_heap.add_appointment(appointment5)
    appointment_heap.add_appointment(appointment6)

    print("Appointments after adding new ones:")
    for app in appointment_heap.view_appointments():
        print(app)

    print("\nProcessing new appointments:")
    while appointment_heap.get_all_appointments():
        print(appointment_heap.pop_appointment())
