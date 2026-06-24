from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict
import uuid

from services.roadmap_service import generate_roadmap

router = APIRouter(
    prefix="/roadmap",
    tags=["Career Roadmap"]
)

# =========================
# In-memory DB (replace with MongoDB/SQL later)
# =========================
ROADMAP_DB: Dict[str, dict] = {}


# =========================
# REQUEST MODEL
# =========================
class RoadmapRequest(BaseModel):
    career_goal: str
    current_skills: List[str] = Field(default_factory=list)  # FIXED
    experience_level: str  # beginner / intermediate / advanced


# =========================
# RESPONSE MODEL
# =========================
class RoadmapResponse(BaseModel):
    roadmap_id: str
    career_goal: str
    steps: List[str]
    resources: List[str]
    estimated_duration: str


# =========================
# CREATE ROADMAP
# =========================
@router.post("/generate", response_model=RoadmapResponse)
async def create_roadmap(request: RoadmapRequest):
    try:
        roadmap_id = str(uuid.uuid4())

        roadmap = generate_roadmap(
            career_goal=request.career_goal,
            skills=request.current_skills,
            level=request.experience_level
        )

        ROADMAP_DB[roadmap_id] = {
            "career_goal": request.career_goal,
            "roadmap": roadmap
        }

        return RoadmapResponse(
            roadmap_id=roadmap_id,
            career_goal=request.career_goal,
            steps=roadmap["steps"],
            resources=roadmap["resources"],
            estimated_duration=roadmap["estimated_duration"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate roadmap: {str(e)}"
        )


# =========================
# GET ROADMAP BY ID
# =========================
@router.get("/{roadmap_id}")
async def get_roadmap(roadmap_id: str):
    roadmap_data = ROADMAP_DB.get(roadmap_id)

    if not roadmap_data:
        raise HTTPException(status_code=404, detail="Roadmap not found")

    return {
        "roadmap_id": roadmap_id,
        "career_goal": roadmap_data["career_goal"],
        "steps": roadmap_data["roadmap"]["steps"],
        "resources": roadmap_data["roadmap"]["resources"],
        "estimated_duration": roadmap_data["roadmap"]["estimated_duration"]
    }