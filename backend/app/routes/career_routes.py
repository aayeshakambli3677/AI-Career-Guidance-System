from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.prompts import career_prompt
from app.services.ai_service import generate_response

router = APIRouter(
    prefix="/career",
    tags=["CareerGPT"]
)


class CareerRequest(BaseModel):
    user_input: str
    profile: dict | None = None


@router.post("/advice")
def get_career_advice(request: CareerRequest):
    profile = request.profile or {}

    prompt = career_prompt(request.user_input, profile)
    ai_response = generate_response(prompt)

    return {
        "status": "success",
        "type": "career_advice",
        "input": request.user_input,
        "profile": profile,
        "response": ai_response
    }