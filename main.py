from fastapi import FastAPI

app = FastAPI()

midTermResults = { 'english': 43, 'math': 27, 'japanese': 62 }

@app.get("/midTermResults")
async def getAllMidTermResults():
    return {"message": "Hello World"}

@app.get("/midTermResults/{subject}")
async def getAllMidTermResult(subject):
    return {"message": "Hello World"}