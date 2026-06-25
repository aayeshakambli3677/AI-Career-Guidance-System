from pydantic import BaseModel, Field
from typing import List, Optional


class CareerRecommendationRequest(BaseModel):
    interests: List[str] = Field(
        ...,
        min_length=1,
        description="User interests used for career matching."
    )

    skills: List[str] = Field(
        default_factory=list,
        description="Current technical and non-technical skills."
    )

    education_level: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Highest educational qualification."
    )

    experience_level: Optional[str] = Field(
        default="Beginner",
        description="User experience level (Beginner, Intermediate, Advanced)."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "interests": [
                    "Artificial Intelligence",
                    "Software Development"
                ],
                "skills": [
                    "Python",
                    "SQL",
                    "Problem Solving"
                ],
                "education_level": "Bachelor of Engineering",
                "experience_level": "Intermediate"
            }
        }
    }


class LearningResource(BaseModel):
    title: str = Field(
        ...,
        description="Recommended learning resource."
    )

    type: str = Field(
        ...,
        description="Resource type (Course, Certification, Book, Website)."
    )


class CareerRecommendation(BaseModel):
    career_title: str = Field(
        ...,
        description="Recommended career role."
    )

    match_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Career compatibility score."
    )

    description: str = Field(
        ...,
        description="Overview of the career path."
    )

    required_skills: List[str] = Field(
        default_factory=list,
        description="Important skills required for this career."
    )

    skill_gaps: List[str] = Field(
        default_factory=list,
        description="Skills the user should learn."
    )

    strengths: List[str] = Field(
        default_factory=list,
        description="User strengths aligned with this career."
    )

    average_salary: Optional[str] = Field(
        default=None,
        description="Estimated salary range."
    )

    job_outlook: Optional[str] = Field(
        default=None,
        description="Future demand and growth prospects."
    )

    learning_resources: List[LearningResource] = Field(
        default_factory=list,
        description="Recommended resources for career preparation."
    )


class CareerRecommendationResponse(BaseModel):
    recommendations: List[CareerRecommendation]

    generated_for: str = Field(
        ...,
        description="Target user profile."
    )

    total_recommendations: int = Field(
        ...,
        ge=0,
        description="Number of recommendations generated."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "generated_for": "Bachelor of Engineering Student",
                "total_recommendations": 1,
                "recommendations": [
                    {
                        "career_title": "Machine Learning Engineer",
                        "match_score": 94.5,
                        "description": "Designs, trains, and deploys machine learning models.",
                        "required_skills": [
                            "Python",
                            "Machine Learning",
                            "Statistics",
                            "Data Structures"
                        ],
                        "skill_gaps": [
                            "Deep Learning",
                            "MLOps"
                        ],
                        "strengths": [
                            "Programming",
                            "Analytical Thinking"
                        ],
                        "average_salary": "₹8-20 LPA",
                        "job_outlook": "High demand with strong future growth.",
                        "learning_resources": [
                            {
                                "title": "Machine Learning Specialization",
                                "type": "Course"
                            },
                            {
                                "title": "Python for Data Science",
                                "type": "Certification"
                            }
                        ]
                    }
                ]
            }
        }
    }