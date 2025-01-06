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
        self.root = TreeNode(hospital_name)  

    def add_department(self, department_name):
        department = TreeNode(department_name)
        self.root.add_child(department)
        return department

    def add_doctor(self, department_node, doctor_name):
        doctor = TreeNode(doctor_name)
        department_node.add_child(doctor)
        return doctor

    def add_appointment(self, doctor_node, patient_name, appointment_details):
        appointment = TreeNode(patient_name, appointment_details)
        doctor_node.add_child(appointment)

    def list_departments(self):
        return [child.name for child in self.root.get_children()]

    def list_doctors(self, department_node):
        return [child.name for child in department_node.get_children()]

    def list_appointments(self, doctor_node):
        appointments = []
        for appointment in doctor_node.get_children():
            appointments.append((appointment.name, appointment.data))
        return appointments


# Example 
if __name__ == "__main__":
    hospital = Hospital("General Hospital")

    cardiology = hospital.add_department("Cardiology")
    neurology = hospital.add_department("Neurology")

    doctor1 = hospital.add_doctor(cardiology, "Dr. emme")
    doctor2 = hospital.add_doctor(cardiology, "Dr. izere")
    doctor3 = hospital.add_doctor(neurology, "Dr. manzi")

    hospital.add_appointment(doctor1, "gisubizo", {"date": "2024-12-25", "time": "10:00 AM"})
    hospital.add_appointment(doctor2, "sandrine", {"date": "2024-12-26", "time": "2:00 PM"})
    hospital.add_appointment(doctor3, "naomi", {"date": "2024-12-27", "time": "1:00 PM"})

    print("Departments in the hospital:", hospital.list_departments())

    print("Doctors in Cardiology:", hospital.list_doctors(cardiology))

    print("Appointments for Dr. emme:", hospital.list_appointments(doctor1))

    print("Appointments for Dr. manzi:", hospital.list_appointments(doctor3))
