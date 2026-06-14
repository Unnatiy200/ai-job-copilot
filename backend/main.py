from fastapi import FastAPI
from api.resume import router as resume_router

app = FastAPI(title="AI Job Copilot")

app.include_router(resume_router, prefix="/resume")

@app.get("/")
def root():
    return {"status": "running"}