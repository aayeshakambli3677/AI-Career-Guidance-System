# repositories/resume_repository.py

from sqlalchemy.orm import Session
from sqlalchemy import desc

from models.resume import Resume


class ResumeRepository:

    @staticmethod
    def create_resume(
        db: Session,
        user_id: int,
        resume_text: str,
        score: int = 0
    ):
        resume = Resume(
            user_id=user_id,
            resume_text=resume_text,
            score=score
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def get_resume_by_id(
        db: Session,
        resume_id: int
    ):
        return (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    @staticmethod
    def get_all_resumes(db: Session):
        return db.query(Resume).all()

    @staticmethod
    def get_resumes_by_user(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Resume)
            .filter(Resume.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_latest_resumes(
        db: Session,
        limit: int = 10
    ):
        return (
            db.query(Resume)
            .order_by(desc(Resume.id))
            .limit(limit)
            .all()
        )

    @staticmethod
    def search_resume(
        db: Session,
        keyword: str
    ):
        return (
            db.query(Resume)
            .filter(
                Resume.resume_text.ilike(f"%{keyword}%")
            )
            .all()
        )

    @staticmethod
    def update_resume(
        db: Session,
        resume_id: int,
        resume_text: str,
        score: int
    ):
        resume = (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

        if not resume:
            return None

        resume.resume_text = resume_text
        resume.score = score

        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def update_score(
        db: Session,
        resume_id: int,
        score: int
    ):
        resume = (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

        if not resume:
            return None

        resume.score = score

        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def delete_resume(
        db: Session,
        resume_id: int
    ):
        resume = (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

        if not resume:
            return None

        db.delete(resume)
        db.commit()

        return resume

    @staticmethod
    def count_resumes(db: Session):
        return db.query(Resume).count()

    @staticmethod
    def resume_exists(
        db: Session,
        resume_id: int
    ):
        return (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
            is not None
        )