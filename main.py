from fastapi import FastAPI
import platform

app = FastAPI()

@app.get("/")
def home():
    return {"message": "System info app is running"}


@app.get("/api/info/")
def get_info():
    return {
        "os": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform()
        },

            }
