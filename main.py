from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# パスパラメータを受け取る
@app.get("/hello/{name}")
async def hello(name):
    return {"message": "Hello {0}".format(name)}