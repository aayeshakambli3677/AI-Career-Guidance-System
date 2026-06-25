# repositories/recommendation_repository.py

from sqlalchemy.orm import Session
from models.recommendation import Recommendation


class RecommendationRepository:

    @staticmethod
    def add_recommendation(
        db: Session,
        user_id: int,
        title: str,
        description: str
    ):
        recommendation = Recommendation(
            user_id=user_id,
            title=title,
            description=description
        )

        db.add(recommendation)
        db.commit()
        db.refresh(recommendation)

        return recommendation

    @staticmethod
    def get_all_recommendations(db: Session):
        return db.query(Recommendation).all()

    @staticmethod
    def get_recommendation_by_id(
        db: Session,
        recommendation_id: int
    ):
        return (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

    @staticmethod
    def get_recommendations_by_user(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Recommendation)
            .filter(Recommendation.user_id == user_id)
            .all()
        )

    @staticmethod
    def update_recommendation(
        db: Session,
        recommendation_id: int,
        title: str,
        description: str
    ):
        recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not recommendation:
            return None

        recommendation.title = title
        recommendation.description = description

        db.commit()
        db.refresh(recommendation)

        return recommendation

    @staticmethod
    def delete_recommendation(
        db: Session,
        recommendation_id: int
    ):
        recommendation = (
            db.query(Recommendation)
            .filter(Recommendation.id == recommendation_id)
            .first()
        )

        if not recommendation:
            return None

        db.delete(recommendation)
        db.commit()

        return recommendation