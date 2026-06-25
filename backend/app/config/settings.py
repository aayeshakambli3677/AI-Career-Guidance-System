from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings
    """

    # =========================
    # PROJECT SETTINGS
    # =========================
    PROJECT_NAME: str = "AI Career Guidance System"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    # =========================
    # DATABASE SETTINGS
    # =========================
    DATABASE_URL: str = "mongodb://localhost:27017/careergpt"

    # =========================
    # SECURITY SETTINGS
    # =========================
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # =========================
    # AI SERVICE SETTINGS
    # =========================
    OPENAI_API_KEY: str = ""

    # =========================
    # CORS SETTINGS
    # =========================
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

    class Config:
        env_file = ".env"


# Global settings instance (use everywhere in project)
settings = Settings()