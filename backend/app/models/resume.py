from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from database import Base


class Resume(Base):
    __tablename__ = "resumes"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Reference
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # Resume Information
    resume_title = Column(
        String(200),
        nullable=False
    )

    resume_text = Column(
        Text,
        nullable=False
    )

    target_role = Column(
        String(100),
        nullable=False,
        index=True
    )

    # Analysis Scores
    overall_score = Column(
        Integer,
        default=0
    )

    ats_score = Column(
        Integer,
        default=0
    )

    # Analysis Results
    strengths = Column(
        Text,
        nullable=True
    )

    improvement_areas = Column(
        Text,
        nullable=True
    )

    missing_keywords = Column(
        Text,
        nullable=True
    )

    recommended_skills = Column(
        Text,
        nullable=True
    )

    recommended_certifications = Column(
        Text,
        nullable=True
    )

    improvement_suggestions = Column(
        Text,
        nullable=True
    )

    final_verdict = Column(
        Text,
        nullable=True
    )

    # Status
    status = Column(
        String(20),
        default="analyzed",
        nullable=False
    )

    # Audit Fields
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    def __repr__(self):
        return (
            f"<Resume("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"target_role='{self.target_role}', "
            f"ats_score={self.ats_score}"
            f")>"
        )