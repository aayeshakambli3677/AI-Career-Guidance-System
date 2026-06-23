from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# -------------------------
# FAKE DB
# -------------------------
users_db = {}

# -------------------------
# PASSWORD HASHING
# -------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# -------------------------
# JWT SETTINGS
# -------------------------
SECRET_KEY = "career_gpt_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# -------------------------
# MODELS
# -------------------------
class UserRegister(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# -------------------------
# CREATE TOKEN FUNCTION
# -------------------------
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

# -------------------------
# REGISTER
# -------------------------
@router.post("/register")
def register(user: UserRegister):

    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    users_db[user.username] = hashed_password

    return {
        "status": "success",
        "message": "User registered successfully"
    }

# -------------------------
# LOGIN (RETURN JWT TOKEN)
# -------------------------
@router.post("/login")
def login(user: UserLogin):

    stored_password = users_db.get(user.username)

    if not stored_password:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = create_access_token({"sub": user.username})

    return {
        "status": "success",
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }

# -------------------------
# PROTECTED ROUTE EXAMPLE
# -------------------------
@router.get("/me")
def get_current_user(token: str):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {
            "status": "success",
            "user": username
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid or expired")