from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the calculator API!"}

@app.get("/plus")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/minus")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/times")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/division")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": a / b}
