from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# リクエストボディを受け取る
@app.post("/study")
async def createStudy(req: Request):
    body = await req.json()
    print(body['name'])
    return body