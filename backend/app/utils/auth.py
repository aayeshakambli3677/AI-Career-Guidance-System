from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# =========================
# CONFIGURATION
# =========================

# CHANGE THESE VALUES YOURSELF
SECRET_KEY = "careergpt_super_secret_key_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# =========================
# PASSWORD HASHING
# =========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Convert plain password into hashed password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Verify user password during login.
    """
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# =========================
# JWT TOKEN FUNCTIONS
# =========================

def create_access_token(
    data: dict,
    expires_delta: timedelta = None
) -> str:
    """
    Generate JWT access token.
    """

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = (
            datetime.utcnow()
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def decode_access_token(
    token: str
):
    """
    Decode JWT token.
    Returns payload if valid.
    Returns None if invalid.
    """

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        return None


# =========================
# HELPER FUNCTION
# =========================

def create_user_token(
    user_id: int,
    email: str
) -> str:
    """
    Generate token for logged-in user.
    """

    payload = {
        "user_id": user_id,
        "email": email
    }

    return create_access_token(payload)