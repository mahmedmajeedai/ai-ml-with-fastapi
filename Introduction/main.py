from fastapi import FastAPI
import json

app = FastAPI()

#helper function to load json data
def load_data():
    with open('Introduction/patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {'message': 'Our first patient API'}

@app.get("/patients")
def get_patients():
    data = load_data()
    return data