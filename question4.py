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

class Node:
    def __init__(self, appointment):
        self.appointment = appointment
        self.left = None
        self.right = None

class AppointmentBinaryTree:
    def __init__(self, max_appointments):
        self.root = None
        self.max_appointments = max_appointments
        self.appointment_count = 0

    def insert(self, appointment):
        if self.appointment_count < self.max_appointments:
            self.root = self._insert(self.root, appointment)
            self.appointment_count += 1
        else:
            print("Maximum number reached. Cannot add more.")

    def _insert(self, node, appointment):
        if node is None:
            return Node(appointment)
        
        if appointment < node.appointment:
            node.left = self._insert(node.left, appointment)
        else:
            node.right = self._insert(node.right, appointment)
        
        return node

    def inorder(self):
        appointments = []
        self._inorder(self.root, appointments)
        return appointments

    def _inorder(self, node, appointments):
        if node:
            self._inorder(node.left, appointments)
            appointments.append(node.appointment)
            self._inorder(node.right, appointments)

    def search(self, appointment_time):
        return self._search(self.root, appointment_time)

    def _search(self, node, appointment_time):
        if node is None:
            return None
        if node.appointment.appointment_time == appointment_time:
            return node.appointment
        elif appointment_time < node.appointment.appointment_time:
            return self._search(node.left, appointment_time)
        else:
            return self._search(node.right, appointment_time)

    def preorder(self):
        appointments = []
        self._preorder(self.root, appointments)
        return appointments

    def _preorder(self, node, appointments):
        if node:
            appointments.append(node.appointment)
            self._preorder(node.left, appointments)
            self._preorder(node.right, appointments)

    def postorder(self):
        appointments = []
        self._postorder(self.root, appointments)
        return appointments

    def _postorder(self, node, appointments):
        if node:
            self._postorder(node.left, appointments)
            self._postorder(node.right, appointments)
            appointments.append(node.appointment)

if __name__ == "__main__":
    appointment_tree = AppointmentBinaryTree(max_appointments=5)

    appointment1 = Appointment("kariza", datetime(2024, 12, 22, 14, 30), 2)
    appointment2 = Appointment("keza", datetime(2024, 12, 22, 9, 0), 3)
    appointment3 = Appointment("sandrine", datetime(2024, 12, 23, 10, 0), 1)
    appointment4 = Appointment("gisubizo", datetime(2024, 12, 22, 13, 30), 2)
    appointment5 = Appointment("prince", datetime(2024, 12, 23, 11, 0), 1)
    appointment6 = Appointment("kazungu", datetime(2024, 12, 22, 16, 0), 2)  

    appointment_tree.insert(appointment1)
    appointment_tree.insert(appointment2)
    appointment_tree.insert(appointment3)
    appointment_tree.insert(appointment4)
    appointment_tree.insert(appointment5)

    appointment_tree.insert(appointment6)

    print("Appointments in Inorder (sorted by priority and time):")
    for app in appointment_tree.inorder():
        print(app)

    print("\nAppointments in Preorder (root first):")
    for app in appointment_tree.preorder():
        print(app)

    print("\nAppointments in Postorder (left and right children first):")
    for app in appointment_tree.postorder():
        print(app)

    search_time = datetime(2024, 12, 22, 14, 30)
    print(f"\nSearching for appointment on {search_time.strftime('%Y-%m-%d %H:%M:%S')}:")
    found_appointment = appointment_tree.search(search_time)
    if found_appointment:
        print(found_appointment)
    else:
        print("No appointment found at this time.")
