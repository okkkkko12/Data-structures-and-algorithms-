import tkinter as tk
from tkinter import messagebox 

# the working code is in the pdf report because we faced some inconvenience with indentations here.

      # Represent medical prescriptions, using the prescription class
class Prescription:
      def __init__(self, patient_id, doctor_id, medication, dosage):
            self.patient_id = patient_id                  # The patient's ID is attached to the prescription
            self.doctor_id = doctor_id                # Doctor id who prescribed the medication
            self.medication = medication                  # Prescription medication
            self.dosage = dosage  

     # Define the hospital management add class
class HospitalManagementApp:
      def __init__(self, root):
            self.root = root
            self.root.title("Hospital Patient Record Management System")
            self.user_role = 'admin'                    # Default user role

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

        # Method to initialize UI elements based on the user role
      def initialize_ui_based_on_role(self):
            self.show_ui_elements_based_on_role()
            print(f"UI initialized for role: {self.user_role}")
        
      # Method to show UI elements based on the user role
      def show_ui_elements_based_on_role(self):
            # Define buttons for different functionalities
            buttons = {
            'add_patient': self.add_patient_button,
            'schedule_appointment': self.schedule_appointment_button,
            'manage_queue': self.manage_queue_button,
            'view_patient_history': self.view_patient_history_button,
            'add_prescription': self.manage_prescriptions_button,
            'generate_reports': self.generate_reports_button,
        }

            # Loop through each button and show or hide based on user permissions
            for action, button in buttons.items():
                  if self.has_permission(action):
                        button.pack(fill=tk.X)   # show the buttom
                  else:
                        button.pack_forget()     # hide the buttom
                        
            # Additional buttons based on specific permission
            if self.has_permission('edit_patient'):
            self.update_patient_button.pack(fill=tk.X)
            self.remove_patient_button.pack(fill=tk.X)

    def update_patient(self):
          # Check if the user has permission to edit patient information
        if not self.has_permission('edit_patient'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
            return

          # Create a new window for updating patient information
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Patient Information")

          # Entry fields for updating patient information
        tk.Label(update_window, text="Patient ID:").pack()
        patient_id_entry = tk.Entry(update_window)
        patient_id_entry.pack()

        tk.Label(update_window, text="Name:").pack()
        name_entry = tk.Entry(update_window)
        name_entry.pack()

        tk.Label(update_window, text="Age:").pack()
        age_entry = tk.Entry(update_window)
        age_entry.pack()

        tk.Label(update_window, text="Medical History (comma-separated):").pack()
        medical_history_entry = tk.Entry(update_window)
        medical_history_entry.pack()

        def update_patient_details():
              # Take updated patient information out of the entry fields.
            patient_id = patient_id_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            medical_history = medical_history_entry.get().split(',')

            # Find and update the patient in the list
            for patient in self.patients_list:
                if patient['patient_id'] == patient_id:
                    patient['name'] = name
                    patient['age'] = age
                    patient['medical_history'] = medical_history
                      # Display success message
                    messagebox.showinfo("Success", f"Patient {name} updated successfully.")
                    update_window.destroy()    # close the update window
                    return
       # Display an error message if the patient cannot be located.
            messagebox.showinfo("Error", "Patient not found.")
       # Button to trigger the update_patient_details function
        tk.Button(update_window, text="Update Patient", command=update_patient_details).pack()

    def remove_patient(self):
          # Create a window to remove a patient
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Patient")

          # Entry field for entering patient ID
        tk.Label(remove_window, text="Patient ID:").pack()
        patient_id_entry = tk.Entry(remove_window)
        patient_id_entry.pack()
          # remove the patient
        tk.Button(remove_window, text="Remove Patient",command=lambda: self.delete_patient(patient_id_entry.get(), remove_window)).pack()

    def delete_patient(self, patient_id, window):
        # Confirmation dialog
        response = messagebox.askyesno("Confirm", "Are you sure you want to remove this patient?")
        if response:
              # Verify that the patient is listed in the patient database.
            patient_found = any(patient['patient_id'] == patient_id for patient in self.patients_list)
            if patient_found:
                # Logic to remove the patient
                self.patients_list = [patient for patient in self.patients_list if patient['patient_id'] != patient_id]
                self.consultation_queue = [patient for patient in self.consultation_queue if
                                           patient['patient_id'] != patient_id]
                  # Display success message
                messagebox.showinfo("Success", "Patient removed successfully.")
            else:
                  # If the patient is not found in the list, display an error message
                messagebox.showinfo("Error", "Patient not found.")
            window.destroy()
        else:
            # If the user decides not to delete, do nothing (the confirmation dialog is closed, but the removal window stays open)
            pass


        # Method for making buttons with various functions
      def create_buttons(self):
        # Creating buttons for different functionalities with instance variables and packing them
            self.add_patient_button = tk.Button(self.main_frame, text="Add New Patient", command=self.add_patient)
            self.schedule_appointment_button = tk.Button(self.main_frame, text="Schedule Appointment",command=self.schedule_appointment)
      
            self.manage_queue_button = tk.Button(self.main_frame, text="Manage Consultation Queue",command=self.manage_queue)
            self.view_patient_history_button = tk.Button(self.main_frame, text="View Patient History", command=self.view_patient_history)
      
            self.manage_prescriptions_button = tk.Button(self.main_frame, text="Manage Prescriptions", command=self.manage_prescriptions)
            self.generate_reports_button = tk.Button(self.main_frame, text="Generate Reports", command=self.generate_reports)
            self.update_patient_button = tk.Button(self.main_frame, text="Update Patient Information",command=self.update_patient)
            self.remove_patient_button = tk.Button(self.main_frame, text="Remove Patient",command=self.remove_patient)
            self.display_queue_button = tk.Button(self.main_frame, text="Display Patient Queue",command=self.display_queue)

            if self.has_permission('manage_queue'):
                  self.display_queue_button.pack(fill=tk.X)
      

        # Adds new patient
      def add_patient(self):
            # Check if the user has permission to add a patient
            if not self.has_permission('add_patient'):
                  messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
                  return
            # Create a new window for adding a patient
            add_patient_window = tk.Toplevel(self.root)
            add_patient_window.title("Add New Patient")

            tk.Label(add_patient_window, text="Patient ID:").pack()  # Add labels and entry fields for patient information
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
            
            # Define a function to dynamically add fields for medical history entry.
            def add_medical_history_entry():
                  entry = tk.Entry(medical_history_frame)
                  entry.pack()
                  medical_history_entries.append(entry)
                  
             # Create a button to add a medical history entry
            tk.Button(add_patient_window, text="Add Medical History Entry", command=add_medical_history_entry).pack()
            add_medical_history_entry() 

            tk.Button(add_patient_window, text="Add Patient",command=lambda: self.save_patient(patient_id_entry.get(),  # Get patient ID from entry field
                                                    name_entry.get(),    # Get name from entry field
                                                    age_entry.get(),     # Get age from entry field
                                                    [entry.get() for entry in medical_history_entries],  # Get medical history from entry fields
                                                    add_patient_window)).pack()


      def save_patient(self, patient_id, name, age, medical_history, window):
            if not self.has_permission('add_patient'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
                  return
                
              # Create a new patient dictionary with the provided information  
            new_patient = {"patient_id": patient_id, "name": name, "age": age, "medical_history": medical_history}
            # Append the new patient to the patients list
            self.patients_list.append(new_patient)
            print(f"Patient {name} added successfully.")    # Print a success message
            window.destroy()        # Close the add patient window
#def function for schedule_appointment to schedual for a patient consultation 

      def schedule_appointment(self):
           if not self.has_permission('schedule_appointment'):
            messagebox.showinfo("Permission Denied", "You do not have permission to perform this action.")
            return
         # Create a new window for scheduling an appointment
        schedule_appointment_window = tk.Toplevel(self.root)
        schedule_appointment_window.title("Schedule Appointment")

# want to assume the existence of a 'Doctor' class to get doctor names
        tk.Label(schedule_appointment_window, text="Patient ID:").pack()
        patient_id_entry = tk.Entry(schedule_appointment_window) #patient info input
        patient_id_entry.pack()
# doctor info input entry lable
        tk.Label(schedule_appointment_window, text="Doctor Name:").pack()
        doctor_name_entry = tk.Entry(schedule_appointment_window)
        doctor_name_entry.pack()
# appointment date info input entry lable
        tk.Label(schedule_appointment_window, text="Appointment Date (YYYY-MM-DD):").pack()
        appointment_date_entry = tk.Entry(schedule_appointment_window)
        appointment_date_entry.pack()
# appointment time info input entry lable
        tk.Label(schedule_appointment_window, text="Appointment Time (HH:MM):").pack()
        appointment_time_entry = tk.Entry(schedule_appointment_window)
        appointment_time_entry.pack()
# creating a button to schedule an appointment
        tk.Button(schedule_appointment_window, text="Schedule",command=lambda: self.save_appointment(patient_id_entry.get(),doctor_name_entry.get(), appointment_date_entry.get(), appointment_time_entry.get(), schedule_appointment_window)).pack()
# then defining a lambda function to call the save_appointment method with the entry values


# new def fucntyino for saving the appointment
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

# How to put a patient in the queue for a consultation
    def add_patient_to_queue(self):
        if self.patients_list:
            for patient in self.patients_list:
                self.consultation_queue.append(patient)  #we want to each patient to the queue
            print("Patients added to the queue.")
        else:
            messagebox.showinfo("Info", "No patients available to add to the queue.")
              
   # Procedure for handling the next patient in the queue for consultation
    def process_next_patient(self):
        if self.consultation_queue:
            next_patient = self.consultation_queue.pop(0)  # Process the first patient in the queue
            patient_name = next_patient['name']  # Get the patient's name from the dictionary
            messagebox.showinfo("Info", f"Processing {patient_name}.")
        else:
            messagebox.showinfo("Info", "No patients in the queue.")


    def display_queue(self):
          # Check if the consultation queue is empty
        if not self.consultation_queue:
            messagebox.showinfo("Queue Empty", "There are no patients in the queue.")
            return
          # Create a new window to display the queue
        queue_window = tk.Toplevel(self.root)
        queue_window.title("Patient Consultation Queue")

        tk.Label(queue_window, text="Patients in Queue:", font=('Arial', 14, 'bold')).pack(pady=10)

        # Display each patient in the queue
        for index, patient in enumerate(self.consultation_queue, start=1):
            patient_info = f"{index}. Patient ID: {patient['patient_id']}, Name: {patient['name']}"
            tk.Label(queue_window, text=patient_info).pack(anchor='w')



      # Method to view patient history
    def view_patient_history(self):
        if self.has_permission('view_patient_history'): #cheking if the user has permission to view patient history
            view_history_window = tk.Toplevel(self.root) #create windown for view patient history
            view_history_window.title("View Patient History")  # create the title of the window

            tk.Label(view_history_window, text="Select Patient:").pack()
            patient_names = [patient['name'] for patient in self.patients_list]
            selected_patient = tk.StringVar()
            selected_patient.set(patient_names[0])  # default value
            patient_menu = tk.OptionMenu(view_history_window, selected_patient, *patient_names)
            patient_menu.pack() # "pack' the dropdown menu into the window

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

# Method to manage prescriptions
    def manage_prescriptions(self):
        if not self.consultation_queue:
            messagebox.showinfo("No Patients", "There are no patients in the consultation queue.")
            return

        if self.has_permission('add_prescription'):
            manage_prescriptions_window = tk.Toplevel(self.root)
            manage_prescriptions_window.title("Manage Prescriptions")

            tk.Label(manage_prescriptions_window, text="Select Patient:").pack()
            patient_names = [patient['name'] for patient in self.consultation_queue]  # Ensure this uses the queue
            selected_patient = tk.StringVar()
            selected_patient.set(patient_names[0] if patient_names else "No patients")
            tk.OptionMenu(manage_prescriptions_window, selected_patient, *patient_names).pack()

            tk.Label(manage_prescriptions_window, text="Medication:").pack()
            medication_entry = tk.Entry(manage_prescriptions_window)
            medication_entry.pack()

            tk.Label(manage_prescriptions_window, text="Dosage:").pack()
            dosage_entry = tk.Entry(manage_prescriptions_window)
            dosage_entry.pack()

            def add_prescription():
                patient_name = selected_patient.get() # Get the name of the selected patient
                patient = next((p for p in self.consultation_queue if p['name'] == patient_name), None)
                if patient:
                    medication = medication_entry.get() #getting the entered medication
                    dosage = dosage_entry.get()
                    if 'medical_history' not in patient or not isinstance(patient['medical_history'], list):
                        patient['medical_history'] = []
                    patient['medical_history'].append(f"Prescription: {medication}, Dosage: {dosage}")
                    messagebox.showinfo("Success", "Prescription added successfully.")
                    # Remove the patient from the consultation queue
                    self.consultation_queue.remove(patient)
                    manage_prescriptions_window.destroy()
                else:
                    messagebox.showinfo("Error", "Patient not found.") #it shows error message if patient not found

            tk.Button(manage_prescriptions_window, text="Add Prescription", command=add_prescription).pack()


      def generate_reports(self):
      # Define the functionality for generating reports here
            pass
            
      def has_permission(self, action):         # How to determine whether the user is authorized to perform a certain use

           # Logic to check if the current user role has permission for the given action
             return action in user_roles_permissions.get(self.user_role, [])
            
   # Set user roles and the permissions that go with them.
user_roles_permissions = {
    'doctor': ['edit', 'add_prescription', 'edit_patient'],
    'nurse': ['edit'],
    'receptionist': ['edit', 'add_patient', 'schedule_appointment'],
    'admin': ['edit', 'add_patient', 'schedule_appointment', 'add_prescription', 'edit_patient', 'manage_queue']
}

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.mainloop()



