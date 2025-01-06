class TreeNode:
    def __init__(self, name, data=None):
        self.name = name  
        self.data = data
        self.children = [] 

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

    def __repr__(self):
        return f"TreeNode({self.name})"


class Hospital:
    def __init__(self, hospital_name):
        self.root = TreeNode(hospital_name)  # Root

    def add_department(self, department_name):
        department = TreeNode(department_name)
        self.root.add_child(department)
        return department

    def add_doctor(self, department_node, doctor_name):
        doctor = TreeNode(doctor_name)
        department_node.add_child(doctor)
        return doctor

    def add_appointment(self, doctor_node, patient_name, appointment_details, priority):
        appointment = TreeNode(patient_name, {'details': appointment_details, 'priority': priority})
        doctor_node.add_child(appointment)

    def list_departments(self):
        return [child.name for child in self.root.get_children()]

    def list_doctors(self, department_node):
        return [child.name for child in department_node.get_children()]

    def list_appointments(self, doctor_node):
        appointments = []
        for appointment in doctor_node.get_children():
            appointments.append((appointment.name, appointment.data['priority'], appointment.data['details']))
        return appointments

    def quick_sort_appointments(self, doctor_node):
        appointments = doctor_node.get_children()
        self.quick_sort(appointments, 0, len(appointments) - 1)
        return [(appointment.name, appointment.data['priority'], appointment.data['details']) for appointment in appointments]

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high].data['priority']
        i = low - 1
        for j in range(low, high):
            if arr[j].data['priority'] < pivot:  
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# Example 
if __name__ == "__main__":
   
    hospital = Hospital("General Hospital")

    cardiology = hospital.add_department("Cardiology")
    neurology = hospital.add_department("Neurology")

    doctor1 = hospital.add_doctor(cardiology, "Dr. emme")
    doctor2 = hospital.add_doctor(cardiology, "Dr. izere")
    doctor3 = hospital.add_doctor(neurology, "Dr. manzi")

    hospital.add_appointment(doctor1, "gisubizo", {"date": "2024-12-25", "time": "10:10 AM"}, priority=2)
    hospital.add_appointment(doctor1, "sandrine", {"date": "2024-12-26", "time": "2:00 PM"}, priority=1)
    hospital.add_appointment(doctor2, "naomi", {"date": "2024-12-27", "time": "1:00 PM"}, priority=3)
    hospital.add_appointment(doctor3, "kazungu", {"date": "2024-12-28", "time": "11:00 AM"}, priority=2)

    print("Departments in the hospital:", hospital.list_departments())

    print("Doctors in Cardiology:", hospital.list_doctors(cardiology))

    print("\nAppointments for Dr. emme (before sorting):")
    appointments = hospital.list_appointments(doctor1)
    for appt in appointments:
        print(f"Patient: {appt[0]}, Priority: {appt[1]}, Details: {appt[2]}")

    sorted_appointments = hospital.quick_sort_appointments(doctor1)
    print("\nAppointments for Dr. emme (after sorting by priority):")
    for appt in sorted_appointments:
        print(f"Patient: {appt[0]}, Priority: {appt[1]}, Details: {appt[2]}")

    print("\nAppointments for Dr. manzi (before sorting):")
    appointments_manzi = hospital.list_appointments(doctor3)
    for appt in appointments_manzi:
        print(f"Patient: {appt[0]}, Priority: {appt[1]}, Details: {appt[2]}")

    sorted_appointments_manzi = hospital.quick_sort_appointments(doctor3)
    print("\nAppointments for Dr. manzi (after sorting by priority):")
    for appt in sorted_appointments_manzi:
        print(f"Patient: {appt[0]}, Priority: {appt[1]}, Details: {appt[2]}")
