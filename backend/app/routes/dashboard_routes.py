from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard():

    return {
        "resumeScore": 85,
        "mockInterviews": 12,
        "skillsLearned": 18,
        "overallProgress": 65,
        "activities": [
            "Resume uploaded successfully",
            "Career recommendation generated",
            "Interview practice completed",
            "Roadmap updated"
        ]
    }