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

from app.database.base import Base


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    career_title = Column(
        String(150),
        nullable=False
    )

    match_score = Column(
        Float,
        default=0.0
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
        default="active"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return (
            f"<Recommendation(id={self.id}, "
            f"career_title='{self.career_title}', "
            f"match_score={self.match_score})>"
        )