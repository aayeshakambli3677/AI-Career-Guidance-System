from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)

from database import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Reference
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # Career Recommendation Details
    career_title = Column(
        String(150),
        nullable=False,
        index=True
    )

    match_score = Column(
        Float,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    required_skills = Column(
        Text,
        nullable=True
    )

    skill_gaps = Column(
        Text,
        nullable=True
    )

    strengths = Column(
        Text,
        nullable=True
    )

    average_salary = Column(
        String(100),
        nullable=True
    )

    job_outlook = Column(
        Text,
        nullable=True
    )

    learning_resources = Column(
        Text,
        nullable=True
    )

    recommendation_status = Column(
        String(20),
        default="active",
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
            f"<Recommendation("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"career_title='{self.career_title}', "
            f"match_score={self.match_score}"
            f")>"
        )