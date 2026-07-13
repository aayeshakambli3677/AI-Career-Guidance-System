from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.db import engine

# Import models
from app.models.user import User

# Import routers
from app.routes.interview_routes import router as interview_router
from app.routes.career_routes import router as career_router
from app.routes.user_routes import router as user_router
from app.routes.resume_routes import router as resume_router
from app.routes.auth_routes import router as auth_router
from app.routes.roadmap_routes import router as roadmap_router
from app.routes import internship_routes
<<<<<<< HEAD
from app.routes.dashboard_routes import router as dashboard_router
from app.models.progress import Progress

=======
# from app.routes.dashboard_routes import router as dashboard_router
>>>>>>> 971fad64266e1a40d464acaf0b3b92d81b17dbd9

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerGPT API",
    description="AI-powered Career Guidance and Interview Preparation System",
    version="1.0.0"
)

# =========================
# CORS CONFIGURATION
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def root():
    return {
        "message": "CareerGPT API is running 🚀",
        "docs": "/docs"
    }

# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# =========================
# INCLUDE ROUTES
# =========================
app.include_router(interview_router)
app.include_router(career_router)
app.include_router(user_router)
app.include_router(resume_router)
app.include_router(auth_router)
app.include_router(roadmap_router)
app.include_router(internship_routes.router)
# app.include_router(dashboard_router)

# =========================
# STARTUP EVENT
# =========================
@app.on_event("startup")
def startup_event():
    print("🚀 CareerGPT Backend Started Successfully")

# =========================
# SHUTDOWN EVENT
# =========================
@app.on_event("shutdown")
def shutdown_event():
    print("🛑 CareerGPT Backend Stopped")