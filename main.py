from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name):
    if len(name) < 3:
        raise HTTPException(status_code=404, detail="Resource not found")
    return {"message": "Hello {0}".format(name)}