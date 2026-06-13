from fastapi import FastAPI

app = FastAPI(title="AI Job Copilot")

@app.get("/")
def root():
    return {"status": "running"}