import tkinter as tk
from tkinter import messagebox 

      # Represent medical prescriptions, using the prescription class
class Prescription:
      def __init__(self, patient_id, doctor_id, medication, dosage):
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
            medical_history_frame = tk.Frame(add_patient_window)
            medical_history_frame.pack()
            medical_history_entries = []

            def add_medical_history_entry():
                  entry = tk.Entry(medical_history_frame)
                  entry.pack()
                  medical_history_entries.append(entry)

            tk.Button(add_patient_window, text="Add Medical History Entry", command=add_medical_history_entry).pack()
            add_medical_history_entry() 

            tk.Button(add_patient_window, text="Add Patient",command=lambda: self.save_patient(patient_id_entry.get(),
                                                    name_entry.get(),
                                                    age_entry.get(),
                                                    [entry.get() for entry in medical_history_entries],
                                                    add_patient_window)).pack()


      def save_patient(self, patient_id, name, age, medical_history, window):
            if not self.has_permission('add_patient'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
                  return
                
                
            new_patient = {"patient_id": patient_id, "name": name, "age": age, "medical_history": medical_history}
            self.patients_list.append(new_patient)
            print(f"Patient {name} added successfully.")
            window.destroy()  # Close the add patient window
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
#doctor info input entry lable
        tk.Label(schedule_appointment_window, text="Doctor Name:").pack()
        doctor_name_entry = tk.Entry(schedule_appointment_window)
        doctor_name_entry.pack()
#appointment date info input entry lable
        tk.Label(schedule_appointment_window, text="Appointment Date (YYYY-MM-DD):").pack()
        appointment_date_entry = tk.Entry(schedule_appointment_window)
        appointment_date_entry.pack()
#appointment time info input entry lable
        tk.Label(schedule_appointment_window, text="Appointment Time (HH:MM):").pack()
        appointment_time_entry = tk.Entry(schedule_appointment_window)
        appointment_time_entry.pack()
#creating a button to schedule an appointment
        tk.Button(schedule_appointment_window, text="Schedule",command=lambda: self.save_appointment(patient_id_entry.get(),doctor_name_entry.get(), appointment_date_entry.get(), appointment_time_entry.get(), schedule_appointment_window)).pack()
#then defining a lambda function to call the save_appointment method with the entry values


#new def fucntyino for saving the appointment
    def save_appointment(self, patient_id, doctor_name, appointment_date, appointment_time, window):
        if not self.has_permission('schedule_appointment'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
            return
        # Save the appointment details, assuming appointments are stored similarly to patients
        appointment = {"patient_id": patient_id, "doctor_name": doctor_name, "date": appointment_date,"time": appointment_time}
        print(f"Appointment scheduled for {patient_id} with {doctor_name} on {appointment_date} at {appointment_time}.")
        window.destroy()  # Close the appointment window

    def manage_queue(self):
          manage_queue_window = tk.Toplevel(self.root)
          manage_queue_window.title("Manage Consultation Queue")
          
          tk.Button(manage_queue_window, text="Add Patient to Queue", command=self.add_patient_to_queue).pack(fill=tk.X)
          tk.Button(manage_queue_window, text="Process Next Patient", command=self.process_next_patient).pack(fill=tk.X)


    def add_patient_to_queue(self):
        if self.patients_list:
            for patient in self.patients_list:
                self.consultation_queue.append(patient)  #we want to each patient to the queue
            print("Patients added to the queue.")
        else:
            messagebox.showinfo("Info", "No patients available to add to the queue.")

    def process_next_patient(self):
        if self.consultation_queue:
            next_patient = self.consultation_queue.pop(0)  # Process the first patient in the queue
            patient_name = next_patient['name']  # Get the patient's name from the dictionary
            messagebox.showinfo("Info", f"Processing {patient_name}.")
        else:
            messagebox.showinfo("Info", "No patients in the queue.")


    def view_patient_history(self):
        if self.has_permission('view_patient_history'):
            view_history_window = tk.Toplevel(self.root)
            view_history_window.title("View Patient History")

            tk.Label(view_history_window, text="Select Patient:").pack()
            patient_names = [patient['name'] for patient in self.patients_list]
            selected_patient = tk.StringVar()
            selected_patient.set(patient_names[0])  # default value
            patient_menu = tk.OptionMenu(view_history_window, selected_patient, *patient_names)
            patient_menu.pack()

            def show_history():
                patient_name = selected_patient.get()
                patient = next((p for p in self.patients_list if p['name'] == patient_name), None)
                if patient:
                    history_text = "\n".join(patient['medical_history'])
                    messagebox.showinfo("Medical History", f"{patient_name}'s History:\n{history_text}")
                else:
                    messagebox.showinfo("Error", "Patient not found.")
                  
            tk.Button(view_history_window, text="Show History", command=show_history).pack()
        else:
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")

    def manage_prescriptions(self):
        if not self.consultation_queue:
            messagebox.showinfo("No Patients", "There are no patients in the consultation queue.")
            




