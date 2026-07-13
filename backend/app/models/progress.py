from sqlalchemy import Column, Integer, Boolean, ForeignKey
from app.database.base import Base

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    profile_completed = Column(Boolean, default=False)

    resume_uploaded = Column(Boolean, default=False)

    resume_analyzed = Column(Boolean, default=False)

    career_completed = Column(Boolean, default=False)

    skills_completed = Column(Boolean, default=False)

    roadmap_completed = Column(Boolean, default=False)

    interview_completed = Column(Boolean, default=False)

    internship_completed = Column(Boolean, default=False)