from fastapi import APIRouter
from app.database.db import SessionLocal
from app.models.user import User
from app.schemas.auth_schema import UserCreate
from passlib.context import CryptContext
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from jose import JWTError
from fastapi import HTTPException

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = "career_gpt_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

class UserLogin(BaseModel):
    email: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

@router.post("/create")
def create_user(user: UserCreate):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        db.close()
        return {
            "message": "Email already registered"
        }

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=pwd_context.hash(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }

@router.post("/login")
def login_user(user: UserLogin):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    if not pwd_context.verify(
        user.password,
        existing_user.password
    ):
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({
        "sub": existing_user.email
    })

    db.close()

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "user_id": existing_user.id,
        "email": existing_user.email,
        "full_name": existing_user.full_name
    }

@router.get("/me")
def get_current_user(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return {
            "message": "Token valid",
            "email": email
        }

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token is invalid or expired"
        )