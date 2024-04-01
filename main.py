import tkinter as tk
from tkinter import messagebox 

     # Patient class for their information
class Patient:
  def __int__(self, name, patient_id, medical_history, condition, admission_date=datetime.datetime.now()):
    self.patient_id = patient_id                             # Patient's id
    self.name = name               
    self.age = age
    self.medical_history=medical_history
    
      # Represent medical prescriptions, using the prescription class
class Prescription:
  def __int__(self, patient_id, doctor_id, medication, dosage):
    self.patient_id = patient_id                  # The patient's ID is attached to the prescription
    self.doctor_id = doctor_id                # Doctor id who prescribed the medication
    self.medication = medication                  # Prescription medication
    self.dosage = dosage  

class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Patient Record Management System")
        self.user_role = 'admin'

        # Initialize data structures
        self.patients_list = []
        self.prescriptions_list = []
        self.consultation_queue = []

        # Initially, hide main UI until role is selected
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # Move button creation to a separate method
        self.create_buttons()
        # Show main UI directly
        self.initialize_ui_based_on_role()

    def initialize_ui_based_on_role(self):
        self.show_ui_elements_based_on_role()
        print(f"UI initialized for role: {self.user_role}")

    def show_ui_elements_based_on_role(self):
        buttons = {
            'add_patient': self.add_patient_button,
            'schedule_appointment': self.schedule_appointment_button,
            'manage_queue': self.manage_queue_button,
            'view_patient_history': self.view_patient_history_button,
            'add_prescription': self.manage_prescriptions_button,
            'generate_reports': self.generate_reports_button,
        }

        for action, button in buttons.items():
            if self.has_permission(action):
                button.pack(fill=tk.X)
            else:
                button.pack_forget()

    def create_buttons(self):
        # Creating buttons for different functionalities with instance variables and packing them
        self.add_patient_button = tk.Button(self.main_frame, text="Add New Patient", command=self.add_patient)
        self.schedule_appointment_button = tk.Button(self.main_frame, text="Schedule Appointment",command=self.schedule_appointment)
      
        self.manage_queue_button = tk.Button(self.main_frame, text="Manage Consultation Queue",command=self.manage_queue)
        self.view_patient_history_button = tk.Button(self.main_frame, text="View Patient History", command=self.view_patient_history)
      
        self.manage_prescriptions_button = tk.Button(self.main_frame, text="Manage Prescriptions", command=self.manage_prescriptions)
        self.generate_reports_button = tk.Button(self.main_frame, text="Generate Reports", command=self.generate_reports)

        def add_patient(self):
        if not self.has_permission('add_patient'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
            return

        add_patient_window = tk.Toplevel(self.root)
        add_patient_window.title("Add New Patient")

        tk.Label(add_patient_window, text="Patient ID:").pack()
        patient_id_entry = tk.Entry(add_patient_window)
        patient_id_entry.pack()

        tk.Label(add_patient_window, text="Name:").pack()
        name_entry = tk.Entry(add_patient_window)
        name_entry.pack()

        tk.Label(add_patient_window, text="Age:").pack()
        age_entry = tk.Entry(add_patient_window)
        age_entry.pack()

        tk.Label(add_patient_window, text="Medical History:").pack()
        medical_history_entry = tk.Entry(add_patient_window)
        medical_history_entry.pack()

        tk.Button(add_patient_window, text="Add Patient",
                  command=lambda: self.save_patient(patient_id_entry.get(),name_entry.get(),age_entry.get(), medical_history_entry.get(),add_patient_window)).pack()

#def function for schedule_appointment to schedual for a patient consultation 
def schedule_appointment(self):
     if not self.has_permission('schedule_appointment'):
          messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
            return

        schedule_appointment_window = tk.Toplevel(self.root)
        schedule_appointment_window.title("Schedule Appointment")

# want to assume the existence of a 'Doctor' class to get doctor names
        tk.Label(schedule_appointment_window, text="Patient ID:").pack()
        patient_id_entry = tk.Entry(schedule_appointment_window) #patient info input
        patient_id_entry.pack()
#doctor info input
        tk.Label(schedule_appointment_window, text="Doctor Name:").pack()
        doctor_name_entry = tk.Entry(schedule_appointment_window)
        doctor_name_entry.pack()
#appointment date info input
        tk.Label(schedule_appointment_window, text="Appointment Date (YYYY-MM-DD):").pack()
        appointment_date_entry = tk.Entry(schedule_appointment_window)
        appointment_date_entry.pack()
#appointment time info input
        tk.Label(schedule_appointment_window, text="Appointment Time (HH:MM):").pack()
        appointment_time_entry = tk.Entry(schedule_appointment_window)
        appointment_time_entry.pack()
