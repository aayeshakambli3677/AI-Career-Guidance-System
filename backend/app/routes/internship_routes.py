from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import generate_response

router = APIRouter(
    prefix="/internship",
    tags=["Internship Recommendation"]
)

class InternshipRequest(BaseModel):
    skills: list[str]
    interest: str

@router.post("/recommend")
async def recommend_internship(data: InternshipRequest):

    prompt = f"""
    Recommend internships for:

    Skills: {data.skills}
    Interest: {data.interest}

    Include:
    1. Internship Roles
    2. Required Skills
    3. Platforms to Apply
    4. Preparation Tips
    """

    response = generate_response(prompt)

    return {
        "success": True,
        "recommendations": response
    }