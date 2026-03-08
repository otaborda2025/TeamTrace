from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "project": "TeamTrace",
        "version": "0.1.0",
        "status": "Online",
        "message": "Hello Orlandy, your API is alive!"
    }