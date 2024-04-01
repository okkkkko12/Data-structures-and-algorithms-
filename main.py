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

class Patient:
  def __int__(self, name, patient_id, medical_history, condition, admission_date=datetime.datetime.now()):
    self.name = name
    self.patient_id = patient_id
    self.medical_history = medical_history
    self.condition = condition
    self.admission_date = admission_date

class Prescription:
  def __int__(self, patient_id, doctor_name, medication, date_issued=datetime.datetime.now()):
    self.patient_id = patient_id
    self.doctor_name = doctor_name
    self.medication = medication
    self.date_issued = date_issued

class Appointment:
  def __int__(self, patient_id, doctor_name, appointment_time):
    self.patient_id = patient_id
    self.doctor_name = doctor_name
    self.appointment_time = appointment_time
