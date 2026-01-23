from pydantic import BaseModel
from typing import List, Dict, Union

class Patient(BaseModel):
    # Type validation
    name: str
    age: int
    allergies: List[str]
    symptoms: List[Union[str, int]] #or X:list
    contact_details: Dict[str, str]


def data_entry():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    allergies = input("Enter patient's allergies (comma-separated): ").split(",")
    symptoms = input("Enter patient's symptoms (comma-separated, can include numbers): ").split(",")
    contact_details = {
        "email": input("Enter patient's email: "),
        "phone": input("Enter patient's phone: ")
    }
    return Patient(
        name=name,
        age=age,
        allergies=allergies,
        symptoms=symptoms,
        contact_details=contact_details
    )

def insert_patient_record(mareez: Patient):
    print(mareez.name)
    print(mareez.age)
    print(mareez.allergies)
    print("Patient record inserted.")

def update_patient_record(mareez: Patient):
    print("Patient record updated.")

patient_data = {
    "name": "Ahmed",
    "age": 23,
    "allergies": ["penicillin", "nuts"],
    "contact_details": {
        "email": "ahmed@example.com",
        "phone": "123-456-7890"
    }
}
# patient1 = Patient(**patient_data)
# insert_patient_record(patient1)
data_entry()