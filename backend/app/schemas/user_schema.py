from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserProfileRequest(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="User's full name."
    )

    email: EmailStr = Field(
        ...,
        description="User email address."
    )

    education_level: str = Field(
        ...,
        description="Highest education qualification."
    )

    career_goal: str = Field(
        ...,
        description="Target career role."
    )

    interests: List[str] = Field(
        default_factory=list,
        description="Areas of interest."
    )

    skills: List[str] = Field(
        default_factory=list,
        description="Current skills."
    )

    experience_level: str = Field(
        default="Beginner",
        description="Beginner, Intermediate, or Advanced."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "full_name": "Sneha Birajdar",
                "email": "sneha@example.com",
                "education_level": "Bachelor of Engineering",
                "career_goal": "Machine Learning Engineer",
                "interests": [
                    "Artificial Intelligence",
                    "Data Science"
                ],
                "skills": [
                    "Python",
                    "SQL",
                    "FastAPI"
                ],
                "experience_level": "Intermediate"
            }
        }
    }


class UserProfileResponse(BaseModel):
    user_id: str = Field(
        ...,
        description="Unique user identifier."
    )

    full_name: str
    email: EmailStr
    education_level: str
    career_goal: str

    interests: List[str] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)

    experience_level: str

    profile_completion: int = Field(
        ...,
        ge=0,
        le=100,
        description="Profile completion percentage."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "user_id": "USR001",
                "full_name": "Sneha Birajdar",
                "email": "sneha@example.com",
                "education_level": "Bachelor of Engineering",
                "career_goal": "Machine Learning Engineer",
                "interests": [
                    "Artificial Intelligence",
                    "Data Science"
                ],
                "skills": [
                    "Python",
                    "SQL",
                    "FastAPI"
                ],
                "experience_level": "Intermediate",
                "profile_completion": 95
            }
        }
    }


class UserUpdateRequest(BaseModel):
    education_level: Optional[str] = None
    career_goal: Optional[str] = None
    interests: Optional[List[str]] = None
    skills: Optional[List[str]] = None
    experience_level: Optional[str] = None