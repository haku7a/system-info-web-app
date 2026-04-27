from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "System info app is running"}
