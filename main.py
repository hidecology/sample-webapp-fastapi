from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# クエリパラメータを受け取る
@app.get("/hello")
async def hello(name):
    return {"message": "Hello {0}".format(name)}