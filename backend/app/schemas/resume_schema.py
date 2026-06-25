from typing import List
from pydantic import BaseModel, Field


class ResumeAnalysisRequest(BaseModel):
    resume_text: str = Field(
        ...,
        min_length=50,
        description="Extracted resume text for analysis."
    )

    target_role: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Target job role."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "resume_text": "Python Developer with experience in FastAPI, SQL, and Machine Learning.",
                "target_role": "Machine Learning Engineer"
            }
        }
    }


class ResumeSectionFeedback(BaseModel):
    section_name: str = Field(
        ...,
        description="Name of the resume section."
    )

    score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Section score."
    )

    feedback: str = Field(
        ...,
        description="Detailed section feedback."
    )


class ResumeAnalysisResponse(BaseModel):
    overall_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Overall resume quality score."
    )

    ats_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="ATS compatibility score."
    )

    strengths: List[str] = Field(
        default_factory=list,
        description="Resume strengths."
    )

    improvement_areas: List[str] = Field(
        default_factory=list,
        description="Areas requiring improvement."
    )

    missing_keywords: List[str] = Field(
        default_factory=list,
        description="Important missing keywords."
    )

    recommended_skills: List[str] = Field(
        default_factory=list,
        description="Suggested skills to learn."
    )

    recommended_certifications: List[str] = Field(
        default_factory=list,
        description="Relevant certifications."
    )

    section_feedback: List[ResumeSectionFeedback] = Field(
        default_factory=list,
        description="Section-wise feedback."
    )

    improvement_suggestions: List[str] = Field(
        default_factory=list,
        description="Actionable improvement suggestions."
    )

    final_verdict: str = Field(
        ...,
        description="Final resume assessment."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "overall_score": 85,
                "ats_score": 82,
                "strengths": [
                    "Strong technical skill set",
                    "Relevant project experience"
                ],
                "improvement_areas": [
                    "Add quantified achievements",
                    "Improve keyword optimization"
                ],
                "missing_keywords": [
                    "TensorFlow",
                    "Docker",
                    "MLOps"
                ],
                "recommended_skills": [
                    "Deep Learning",
                    "Cloud Computing"
                ],
                "recommended_certifications": [
                    "AWS Certified Cloud Practitioner",
                    "Google Data Analytics"
                ],
                "section_feedback": [
                    {
                        "section_name": "Projects",
                        "score": 88,
                        "feedback": "Projects are relevant and well-described."
                    },
                    {
                        "section_name": "Skills",
                        "score": 80,
                        "feedback": "Add more industry-specific skills."
                    }
                ],
                "improvement_suggestions": [
                    "Include measurable achievements.",
                    "Add role-specific keywords."
                ],
                "final_verdict": "Strong resume with good ATS potential. Minor improvements can significantly increase interview chances."
            }
        }
    }