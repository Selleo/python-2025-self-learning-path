from fastapi import FastAPI

app = FastAPI(title="Service Booking API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Service Booking API!"}
