import heapq
from datetime import datetime

class Appointment:
    def __init__(self, patient_name, appointment_date, priority):
        self.patient_name = patient_name
        self.appointment_date = appointment_date 
        self.priority = priority  

    def __lt__(self, other):
        return (self.priority, self.appointment_date) < (other.priority, other.appointment_date)

    def __repr__(self):
        return f"{self.patient_name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')} with Priority {self.priority}"

class AppointmentHeap:
    def __init__(self):
        self.heap = []

    def add_appointment(self, appointment):
        heapq.heappush(self.heap, appointment)

    def pop_appointment(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def view_appointments(self):
        return sorted(self.heap, key=lambda x: (x.priority, x.appointment_date))

class Node:
    def __init__(self, appointment):
        self.appointment = appointment
        self.left = None
        self.right = None

class AppointmentBST:
    def __init__(self):
        self.root = None

    def insert(self, appointment):
        if self.root is None:
            self.root = Node(appointment)
        else:
            self._insert(self.root, appointment)

    def _insert(self, node, appointment):
        if appointment.appointment_date < node.appointment.appointment_date:
            if node.left is None:
                node.left = Node(appointment)
            else:
                self._insert(node.left, appointment)
        else:
            if node.right is None:
                node.right = Node(appointment)
            else:
                self._insert(node.right, appointment)

    def search_by_date(self, appointment_date):
        return self._search_by_date(self.root, appointment_date)

    def _search_by_date(self, node, appointment_date):
        if node is None:
            return None
        if node.appointment.appointment_date == appointment_date:
            return node.appointment
        elif appointment_date < node.appointment.appointment_date:
            return self._search_by_date(node.left, appointment_date)
        else:
            return self._search_by_date(node.right, appointment_date)

    def inorder(self):
        appointments = []
        self._inorder(self.root, appointments)
        return appointments

    def _inorder(self, node, appointments):
        if node:
            self._inorder(node.left, appointments)
            appointments.append(node.appointment)
            self._inorder(node.right, appointments)

# Example 
if __name__ == "__main__":
    appointment_heap = AppointmentHeap()
    appointment_bst = AppointmentBST()

    appointment1 = Appointment("gisubizo", datetime(2024, 12, 22, 14, 30), 1)
    appointment2 = Appointment("kalisa", datetime(2024, 12, 22, 9, 7), 3)
    appointment3 = Appointment("prince", datetime(2024, 12, 23, 10, 0), 2)
    appointment4 = Appointment("sandrine", datetime(2024, 12, 22, 13, 30), 8)

    appointment_heap.add_appointment(appointment1)
    appointment_heap.add_appointment(appointment2)
    appointment_heap.add_appointment(appointment3)
    appointment_heap.add_appointment(appointment4)

    print("Appointments (Heap ordered by priority):")
    for app in appointment_heap.view_appointments():
        print(app)

    appointment_bst.insert(appointment1)
    appointment_bst.insert(appointment2)
    appointment_bst.insert(appointment3)
    appointment_bst.insert(appointment4)

    print("\nAppointments (BST ordered by date):")
    for app in appointment_bst.inorder():
        print(app)

    search_date = datetime(2024, 12, 22, 13, 30)
    print(f"\nSearching for appointment on {search_date.strftime('%Y-%m-%d %H:%M:%S')}:")
    found_appointment = appointment_bst.search_by_date(search_date)
    if found_appointment:
        print(found_appointment)
    else:
        print("No appointment found on this date.")

    print("\nPopping the highest priority appointment:")
    highest_priority_appointment = appointment_heap.pop_appointment()
    print(highest_priority_appointment)
