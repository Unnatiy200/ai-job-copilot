from fastapi import APIRouter, UploadFile, File
from agents.resume_parser import parse_resume
from agents.resume_agent import analyze_resume
import shutil, os

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # Save file
    file_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Parse + Analyze
    text = parse_resume(file_path)
    analysis = analyze_resume(text)
    
    return {"analysis": analysis}