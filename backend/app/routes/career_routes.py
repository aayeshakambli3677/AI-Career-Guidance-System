from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.prompts import career_prompt
from app.database.db import SessionLocal
from app.models.recommendation import Recommendation

router = APIRouter(
    prefix="/career",
    tags=["CareerGPT"]
)

# -------------------------
# REQUEST MODEL
# -------------------------
class CareerRequest(BaseModel):
    user_input: str
    profile: dict = None   # FIXED (avoid mutable default)

# -------------------------
# CAREER ADVICE
# -------------------------
@router.post("/advice")
def get_career_advice(request: CareerRequest):

    profile = request.profile or {}

    prompt = career_prompt(request.user_input, profile)
    db = SessionLocal()
    new_rec = Recommendation(
        user_id=1,
        career_title=request.user_input,
        match_score=90,
        description=prompt
        )
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    db.close()

    return {
        "status": "success",
        "type": "career_advice",
        "input": request.user_input,
        "profile": profile,
        "response": prompt
    }

# -------------------------
# SKILL SUGGESTION
# -------------------------
@router.post("/skills")
def suggest_skills(request: CareerRequest):

    profile = request.profile or {}

    prompt = f"""
You are CareerGPT AI.

User Input: {request.user_input}
Profile: {profile}

Suggest:
- Top skills required
- Tools to learn
- Career direction
"""

    return {
        "status": "success",
        "type": "skill_suggestion",
        "response": prompt
    }

# -------------------------
# CAREER ROADMAP
# -------------------------
@router.post("/roadmap")
def career_roadmap(request: CareerRequest):

    profile = request.profile or {}

    prompt = f"""
Create a complete career roadmap:

User Input: {request.user_input}
Profile: {profile}

Include:
1. Required Skills
2. Step-by-step learning path
3. Timeline
4. Free resources
"""

    return {
        "status": "success",
        "type": "roadmap",
        "response": prompt
    }