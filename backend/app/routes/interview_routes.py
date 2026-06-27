from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import generate_response
from app.database.db import SessionLocal
from app.models.interview import Interview

router = APIRouter(
    prefix="/interview",
    tags=["Interview Preparation"]
)

# =========================
# MODELS
# =========================

class InterviewRequest(BaseModel):
    role: str
    experience_level: str = "Fresher"


class AnswerEvaluation(BaseModel):
    role: str
    question: str
    answer: str


# =========================
# GENERATE QUESTIONS
# =========================

@router.post("/questions")
async def generate_interview_questions(data: InterviewRequest):

    prompt = f"""
    Generate 10 professional interview questions.

    Role: {data.role}
    Experience Level: {data.experience_level}

    Include:
    1. Technical Questions
    2. HR Questions
    3. Scenario Based Questions

    Return numbered questions.
    """

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "role": data.role,
            "experience_level": data.experience_level,
            "questions": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# MOCK INTERVIEW
# =========================

@router.post("/mock-interview")
async def mock_interview(data: InterviewRequest):

    prompt = f"""
    Act as a professional interviewer.

    Candidate Role: {data.role}
    Experience Level: {data.experience_level}

    Ask one interview question only.
    """

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "question": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# ANSWER EVALUATION
# =========================

@router.post("/evaluate")
async def evaluate_answer(data: AnswerEvaluation):

    prompt = f"""
    Evaluate the following interview answer.

    Role:
    {data.role}

    Question:
    {data.question}

    Candidate Answer:
    {data.answer}

    Give:
    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improvement Suggestions
    5. Better Sample Answer
    """

    try:
        response = generate_response(prompt)
        db = SessionLocal()

        new_interview = Interview(
            user_id=1,
            interview_type="technical",
            career_domain=data.role,
            experience_level="Fresher",
            question=data.question,
            user_answer=data.answer,
            feedback=response,
            score=8
            )
        db.add(new_interview)
        db.commit()
        db.refresh(new_interview)
        db.close()

        return {
            "success": True,
            "feedback": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# HR QUESTIONS
# =========================

@router.get("/hr-questions")
async def hr_questions():

    prompt = """
    Generate Top 20 HR Interview Questions
    with short sample answers.
    """

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "questions": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# TECHNICAL QUESTIONS
# =========================

@router.get("/technical/{role}")
async def technical_questions(role: str):

    prompt = f"""
    Generate Top 20 Technical Interview Questions
    for {role} with answers.
    """

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "role": role,
            "questions": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# INTERVIEW TIPS
# =========================

@router.get("/tips/{role}")
async def interview_tips(role: str):

    prompt = f"""
    Give professional interview preparation tips for {role}.

    Include:
    - Resume Tips
    - Technical Preparation
    - HR Preparation
    - Communication Tips
    - Common Mistakes
    """

    try:
        response = generate_response(prompt)

        return {
            "success": True,
            "role": role,
            "tips": response
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )