"""
Course: Object-Oriented Programming 1 (PROG211)
Assignment: Real-World Solutions under DPG Standards
Domain: Health - Vaccination Tracker & Patient Record System
Author: Amadu Jalloh
Student ID: 905005971
"""

class VaccineRecord:
    def __init__(self, vaccine_name: str, dose_number: int, date_administered: str):
        self.vaccine_name = vaccine_name
        self.dose_number = dose_number
        self.date_administered = date_administered

    def get_details(self) -> str:
        """Returns formatted string of vaccination details."""
        return f"{self.vaccine_name} (Dose {self.dose_number}) on {self.date_administered}"


class Patient:
    # Class attribute to track total patients registered across system
    total_patients_registered = 0

    def __init__(self, patient_id: str, raw_name: str, age: int, location_coords: tuple):
        self.patient_id = patient_id
        # DPG Privacy Standard: name is automatically anonymized using static method
        self.name = Patient.anonymize_name(raw_name)
        self.age = age
        # Tuple data structure implementation (Latitude, Longitude) for Extra 10 Marks
        self.location_coords = location_coords
        self.vaccinations = []  # List of VaccineRecord objects

        # Increment global patient counter
        Patient.total_patients_registered += 1

    # Instance Method
    def update_record(self, vaccine_name: str, dose_number: int, date_administered: str):
        """Adds a new VaccineRecord object to the patient's record."""
        record = VaccineRecord(vaccine_name, dose_number, date_administered)
        self.vaccinations.append(record)

    # Instance Method
    def display_info(self):
        """Displays patient details and vaccination history."""
        print(f"\n--- Patient Record [{self.patient_id}] ---")
        print(f"Name (Anonymized for Privacy): {self.name}")
        print(f"Age: {self.age}")
        print(f"Location Coords (Lat, Long): {self.location_coords}")
        print("Vaccination History:")
        if not self.vaccinations:
            print(" - No records found.")
        else:
            for v in self.vaccinations:
                print(f" - {v.get_details()}")

    # Class Method
    @classmethod
    def get_total_patients(cls) -> int:
        """Returns the total number of patient instances created."""
        return cls.total_patients_registered

    # Static Method (DPG Privacy Compliance)
    @staticmethod
    def anonymize_name(full_name: str) -> str:
        """
        Anonymizes names to comply with DPG privacy principles.
        Example: 'John Doe' -> 'J. D.'
        """
        parts = full_name.strip().split()
        if not parts:
            return "Anonymous"
        return " ".join([f"{p[0].upper()}." for p in parts])


class VaccinationTrackerSystem:
    def __init__(self):
        # Dictionary data structure storing patients with patient_id as key
        self.patient_registry = {}

    def add_patient(self, patient: Patient):
        """Adds a patient object to the dictionary database."""
        self.patient_registry[patient.patient_id] = patient
        print(f"\nSUCCESS: Patient [{patient.patient_id}] successfully added.")

    def get_patient(self, patient_id: str) -> Patient:
        """Retrieves a patient object by ID."""
        return self.patient_registry.get(patient_id, None)

    def display_all_records(self):
        """Loops through and displays all patients in the registry."""
        print("\n================ ALL PATIENT RECORDS ================")
        if not self.patient_registry:
            print("No records stored in the system yet.")
        for p_id, patient_obj in self.patient_registry.items():
            patient_obj.display_info()
        print("=====================================================")


# Interactive Terminal Menu
if __name__ == "__main__":
    system = VaccinationTrackerSystem()

    while True:
        print("\n=== VACCINATION TRACKER SYSTEM (DPG COMPLIANT) ===")
        print("1. Register New Patient")
        print("2. Add Vaccination Record to Existing Patient")
        print("3. View All Patient Records")
        print("4. View Total Patient Count")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            p_id = input("Enter Patient ID (e.g., P101): ").strip()
            name = input("Enter Patient Full Name: ").strip()
            age = int(input("Enter Patient Age: "))
            
            # Entering Tuple values (Latitude and Longitude)
            print("Enter Health Center Coordinates:")
            lat = float(input("  Latitude (e.g., 8.4844): "))
            long = float(input("  Longitude (e.g., -13.2344): "))
            coords = (lat, long)  # Tuple created

            new_patient = Patient(patient_id=p_id, raw_name=name, age=age, location_coords=coords)
            system.add_patient(new_patient)

        elif choice == "2":
            p_id = input("Enter Patient ID to update: ").strip()
            patient = system.get_patient(p_id)
            
            if patient:
                v_name = input("Enter Vaccine Name (e.g., Pfizer, Yellow Fever): ").strip()
                dose = int(input("Enter Dose Number (e.g., 1, 2): "))
                date = input("Enter Date Administered (YYYY-MM-DD): ").strip()
                
                patient.update_record(v_name, dose, date)
                print(f"SUCCESS: Vaccine record added for patient [{p_id}].")
            else:
                print("ERROR: Patient ID not found.")

        elif choice == "3":
            system.display_all_records()

        elif choice == "4":
            # Class method call
            print(f"\nTotal Patients Registered in System: {Patient.get_total_patients()}")

        elif choice == "5":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose options 1 to 5.")