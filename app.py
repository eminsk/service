from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Welcome in my service"}
