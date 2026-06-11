from fastapi import FastAPI
from pydantic import BaseModel

Dummy_data= [{
    "id" : "shantanu",
    "Company": "BOSCH",
    "EXP": 4},
    {
    "id" : "Sony",
    "Company": "Capgemini",
    "EXP": 7}
]
#GET
app = FastAPI()
@app.get("/get/all")
def get_all():
    return Dummy_data

@app.get("/app/{id}")
def get_ele_byID(id):
    for element in Dummy_data:
        if element["id"]== id:
            return element


#POST
class MyClass(BaseModel):
    id : str
    Company: str
    EXP: int

@app.post("/add_data")
def add_data(add_data: MyClass):
    for elemennt in Dummy_data:
        if elemennt["id"]==add_data.id:
            return {"message": "ID already exists"}
        Dummy_data.append(add_data.model_dump())
        return {
        "message": "Data Added Successfully",
        "data": add_data
        }
