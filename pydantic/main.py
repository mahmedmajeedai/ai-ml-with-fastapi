from pydantic import BaseModel

class Patient(BaseModel):
    # Type validation
    name: str
    age: int

def insert_patient_record(mareez: Patient):
    print(mareez.name)
    print(mareez.age)
    print(type(mareez.age))
    print("Patient record inserted.")

def update_patient_record(mareez: Patient):
    print("Patient record updated.")

patient_data = {
    "name": "Ahmed",
    "age": 23
}
patient1 = Patient(**patient_data)
insert_patient_record(patient1)