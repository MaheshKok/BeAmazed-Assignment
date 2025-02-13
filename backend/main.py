from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from api import intro
from limiter import limiter
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Advanced YouTube Intro Generator API",
    description="API to generate catchy YouTube intros using OpenAI's GPT-3/4.",
    version="1.0.0"
)

# CORS configuration (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your specific domains in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the rate limiter with the FastAPI app state
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded. Try again later."}
    )

# Include the intro router with a prefix
app.include_router(intro.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Advanced YouTube Intro Generator API!"}