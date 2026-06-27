from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from app.database.db import SessionLocal
from app.models.resume import Resume
import uuid

from app.services.resume_service import (
    extract_text_from_file,
    analyze_resume_text
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Management"]
)

# In-memory DB (replace with real DB later)
RESUME_DB: Dict[str, dict] = {}


# =========================
# RESPONSE MODELS
# =========================
class ResumeResponse(BaseModel):
    resume_id: str
    filename: str
    message: str


class AnalysisResponse(BaseModel):
    resume_id: str
    ats_score: int
    feedback: str
    strengths: List[str]
    improvements: List[str]


# =========================
# UPLOAD RESUME
# =========================
@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are supported"
        )

    resume_id = str(uuid.uuid4())

    # FIX 1: removed unsafe await (assuming sync function)
    content = extract_text_from_file(file)

    RESUME_DB[resume_id] = {
        "filename": file.filename,
        "content": content
    }

    return ResumeResponse(
        resume_id=resume_id,
        filename=file.filename,
        message="Resume uploaded successfully"
    )


# =========================
# ANALYZE RESUME
# =========================
@router.get("/analyze/{resume_id}", response_model=AnalysisResponse)
async def analyze_resume(resume_id: str):
    resume = RESUME_DB.get(resume_id)

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    analysis = analyze_resume_text(resume["content"])
    db = SessionLocal()
    new_resume = Resume(
        user_id=1,
        resume_title=resume["filename"],
        resume_text=resume["content"],
        target_role="Software Developer",
        ats_score=analysis["ats_score"],
        strengths=str(analysis["strengths"]),
        improvement_areas=str(analysis["improvements"])
        )
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    db.close()

    return AnalysisResponse(
        resume_id=resume_id,
        ats_score=analysis["ats_score"],
        feedback=analysis["feedback"],
        strengths=analysis["strengths"],
        improvements=analysis["improvements"]
    )


# =========================
# GET RESUME INFO
# =========================
@router.get("/{resume_id}")
async def get_resume(resume_id: str):
    resume = RESUME_DB.get(resume_id)

    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    return {
        "resume_id": resume_id,
        "filename": resume["filename"],
        "content_preview": resume["content"][:300]
    }