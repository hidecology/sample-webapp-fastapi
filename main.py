from fastapi import FastAPI, HTTPException

app = FastAPI()

midTermResults = { 'english': 43, 'math': 27, 'japanese': 62 }

@app.get("/midTermResults")
async def getAllMidTermResults():
    return midTermResults

@app.get("/midTermResults/{subject}")
async def getAllMidTermResult(subject):
    try:
        result = midTermResults[subject]
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail="Resource not found")
