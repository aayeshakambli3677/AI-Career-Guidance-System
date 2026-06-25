from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from database import Base


class Interview(Base):
    __tablename__ = "interviews"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # User Reference
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    # Interview Metadata
    interview_type = Column(
        String(50),
        nullable=False,
        default="technical"
    )

    career_domain = Column(
        String(100),
        nullable=False,
        index=True
    )

    experience_level = Column(
        String(50),
        nullable=False
    )

    # Question & Answer
    question = Column(
        Text,
        nullable=False
    )

    user_answer = Column(
        Text,
        nullable=True
    )

    suggested_answer = Column(
        Text,
        nullable=True
    )

    # AI Evaluation
    score = Column(
        Integer,
        default=0
    )

    feedback = Column(
        Text,
        nullable=True
    )

    strengths = Column(
        Text,
        nullable=True
    )

    improvement_areas = Column(
        Text,
        nullable=True
    )

    # Interview Status
    status = Column(
        String(20),
        default="completed",
        nullable=False
    )

    # Timestamps
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
            f"<Interview("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"career_domain='{self.career_domain}', "
            f"score={self.score}"
            f")>"
        )