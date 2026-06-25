# repositories/user_repository.py

from sqlalchemy.orm import Session
from sqlalchemy import desc

from models.user import User


class UserRepository:

    @staticmethod
    def create_user(
        db: Session,
        full_name: str,
        email: str
    ):
        user = User(
            full_name=full_name,
            email=email
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def get_latest_users(
        db: Session,
        limit: int = 10
    ):
        return (
            db.query(User)
            .order_by(desc(User.id))
            .limit(limit)
            .all()
        )

    @staticmethod
    def search_users(
        db: Session,
        keyword: str
    ):
        return (
            db.query(User)
            .filter(
                User.full_name.ilike(f"%{keyword}%")
            )
            .all()
        )

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        full_name: str,
        email: str
    ):
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return None

        user.full_name = full_name
        user.email = email

        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int
    ):
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user

    @staticmethod
    def count_users(db: Session):
        return db.query(User).count()

    @staticmethod
    def user_exists(
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
            is not None
        )