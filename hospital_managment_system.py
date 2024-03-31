from collections import deque

class Patient:
    def __init__(self, patient_id, name, medical_history, current_condition):
        self.patient_id = patient_id
        self.name = name
        self.medical_history = medical_history
        self.current_condition = current_condition
        self.prescriptions = []

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, patient, doctor, appointment_time):
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

class Prescription:
    def __init__(self, patient, doctor, medication, dosage):
        self.patient = patient
        self.doctor = doctor
        self.medication = medication
        self.dosage = dosage

class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}  # Dictionary to store patient records
        self.doctors = {}   # Dictionary to store doctor records
        self.waiting_queue = deque()  # Queue to maintain line of patients waiting for consultation
        self.appointments = {}  # Dictionary to manage appointments
        self.prescriptions = []  # List to manage prescriptions

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def update_patient_record(self, patient_id, new_details):
        if patient_id in self.patients:
            for key, value in new_details.items():
                setattr(self.patients[patient_id], key, value)

    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]

    def schedule_appointment(self, patient_id, doctor_id, time):
        if patient_id in self.patients and doctor_id in self.doctors:
            appointment = Appointment(self.patients[patient_id], self.doctors[doctor_id], time)
            self.appointments[patient_id] = appointment

    def manage_consultation_queue(self):
        return self.waiting_queue.popleft() if self.waiting_queue else None

    def issue_prescription(self, patient_id, doctor_id, medication, dosage):
        if patient_id in self.patients and doctor_id in self.doctors:
            prescription = Prescription(self.patients[patient_id], self.doctors[doctor_id], medication, dosage)
            self.prescriptions.append(prescription)
            self.patients[patient_id].prescriptions.append(prescription)

    def search_patient(self, patient_id):
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            appointment = self.appointments.get(patient_id)
            return {
                'Patient ID': patient.patient_id,
                'Name': patient.name,
                'Medical History': patient.medical_history,
                'Current Condition': patient.current_condition,
                'Doctor': appointment.doctor.name if appointment else 'Not scheduled',
                'Appointment Time': appointment.appointment_time if appointment else 'Not scheduled',
                'Medications': [prescription.medication for prescription in patient.prescriptions]
            }
        else:
            return None

# You can continue the GUI implementation and testing as before, considering these modifications.