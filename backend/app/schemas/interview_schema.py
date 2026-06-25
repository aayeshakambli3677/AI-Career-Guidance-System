from pydantic import BaseModel, Field
from typing import List


class InterviewQuestionRequest(BaseModel):
    career_domain: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Target career domain for interview preparation.",
        examples=["Python Developer"]
    )

    experience_level: str = Field(
        ...,
        description="Candidate experience level.",
        examples=["Beginner"]
    )

    number_of_questions: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Number of interview questions to generate."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "career_domain": "Python Developer",
                "experience_level": "Intermediate",
                "number_of_questions": 5
            }
        }
    }


class InterviewQuestionResponse(BaseModel):
    questions: List[str] = Field(
        ...,
        description="List of generated interview questions."
    )

    total_questions: int = Field(
        ...,
        description="Total number of questions generated."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "questions": [
                    "Explain Python decorators.",
                    "What is multithreading in Python?",
                    "What is FastAPI?"
                ],
                "total_questions": 3
            }
        }
    }


class InterviewAnswerRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=5,
        description="Interview question answered by the user."
    )

    answer: str = Field(
        ...,
        min_length=10,
        description="User's answer to the interview question."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "question": "What is FastAPI?",
                "answer": "FastAPI is a modern Python framework used for building APIs."
            }
        }
    }


class InterviewAnswerResponse(BaseModel):
    score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Evaluation score assigned to the answer."
    )

    feedback: str = Field(
        ...,
        description="Detailed feedback on the submitted answer."
    )

    strengths: List[str] = Field(
        default_factory=list,
        description="Positive aspects of the answer."
    )

    improvements: List[str] = Field(
        default_factory=list,
        description="Areas where the answer can be improved."
    )

    suggested_answer: str = Field(
        ...,
        description="Recommended answer for learning purposes."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "score": 85,
                "feedback": "Good understanding of the concept.",
                "strengths": [
                    "Clear explanation",
                    "Relevant examples"
                ],
                "improvements": [
                    "Add more technical depth"
                ],
                "suggested_answer": "FastAPI is a high-performance Python framework for building REST APIs using type hints."
            }
        }
    }