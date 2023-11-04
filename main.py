from fastapi import FastAPI
from pydantic import BaseModel

class StudentRecord(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# リクエストボディを受け取る
@app.post("/study")
async def createStudy(rec: StudentRecord):
    print(rec.name, rec.age)
    return rec.name