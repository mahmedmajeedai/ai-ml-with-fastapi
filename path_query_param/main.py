from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

#helper function to load json data
def load_data():
    with open('/home/muhammad-ahmed/Documents/fastapi/ai-ml-with-fastapi/http_method/patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {'message': 'Our first patient API'}

@app.get("/view")
def view():
    data = load_data()
    return data

# path param
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(
    ...,
    description="This information is for patient ID",
    example="1"
    )):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description="Field to sort by", example="age"),
    order: str = Query(..., description="Sort order", example="asc")
):
    valid_fields = "age"
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order")
    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.items(), key=lambda x: x[1][sort_by], reverse=sort_order)
    return dict(sorted_data)