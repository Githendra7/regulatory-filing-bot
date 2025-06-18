from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def first():
    return {"id":1, "content":"Hello World!"}