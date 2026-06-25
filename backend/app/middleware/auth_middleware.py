from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from utils.jwt_handler import verify_token


class AuthMiddleware(BaseHTTPMiddleware):
    """
    JWT Authentication Middleware
    Protects routes by validating Bearer token
    """

    def __init__(self, app):
        super().__init__(app)

        # Public routes (no auth required)
        self.public_paths = {
            "/docs",
            "/openapi.json",
            "/redoc",
            "/auth/login",
            "/auth/register"
        }

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # Allow public routes
        if path in self.public_paths or path.startswith("/static"):
            return await call_next(request)

        # Get Authorization header
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return JSONResponse(
                status_code=401,
                content={"detail": "Authorization header missing"}
            )

        # Validate Bearer token format safely
        parts = auth_header.split()

        if len(parts) != 2:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid authorization format"}
            )

        scheme, token = parts

        if scheme.lower() != "bearer":
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid auth scheme"}
            )

        try:
            # Verify JWT token
            payload = verify_token(token)

            # Attach user info to request
            request.state.user = payload

        except Exception:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or expired token"}
            )

        # Continue request
        response = await call_next(request)
        return response