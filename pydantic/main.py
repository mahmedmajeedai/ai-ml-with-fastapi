from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    # Type validation
    name: str
    age: int
    allergies: List[str]
    contact_details: Dict[str, str]

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
patient1 = Patient(**patient_data)
insert_patient_record(patient1)