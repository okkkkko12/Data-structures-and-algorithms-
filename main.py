import datetime

class User:    # Creating user class to represent the user of the system
  def __init__(self, employee_id, name, role):
      self.employee_id = employee_id
      self.name = name               # User name
      self.role = role               # Any kind of rule(doctor, receptionist)
    
class authorized_user:    # A class to manage and handle user authentication
    users = []                       # A class variable to hold the system users list

    @classmethod
    def add_user(cls, user):
        cls.users.append(user)       # Will add new user to the list

    @classmethod
    def authenticate(cls, employee_id, name):
        # Verify a user's identity using their name and employee ID.
        for user in cls.users:
            if user.employee_id == employee_id and user.name == name:
                return user          # If found, it's will return user object
        return None                  # Will return None if authentication fails

     # Patient class for their information
class Patient:
  def __int__(self, name, patient_id, medical_history, condition, admission_date=datetime.datetime.now()):
    self.name = name                             # Patient's name
    self.patient_id = patient_id                 # Patient's own id number
    self.medical_history = medical_history       # Patient medical history
    self.condition = condition                   # Patient current medical condition
    self.admission_date = admission_date         # Admission date
    
      # Represent medical prescriptions, using the prescription class
class Prescription:
  def __int__(self, patient_id, doctor_name, medication, date_issued=datetime.datetime.now()):
    self.patient_id = patient_id                  # The patient's ID is attached to the prescription
    self.doctor_name = doctor_name                # Doctor name who prescribed the medication
    self.medication = medication                  # Prescription medication
    self.date_issued = date_issued                # The date on which the prescription was completed

      # Appointment class to manage betweens patients and doctors appointments
class Appointment:
  def __int__(self, patient_id, doctor_name, appointment_time):
    self.patient_id = patient_id                  # Id of the patient booked appointment
    self.doctor_name = doctor_name                # Appointment doctor name
    self.appointment_time = appointment_time      # Appointment time
