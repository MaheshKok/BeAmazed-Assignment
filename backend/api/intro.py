from fastapi import APIRouter, HTTPException, Request
from models import ScriptRequest, IntroResponse
from services.openai_service import generate_youtube_intro
from limiter import limiter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/generate-intro", response_model=IntroResponse)
@limiter.limit("5/minute")  # Allow max 5 requests per minute per IP
async def generate_intro(request: Request, payload: ScriptRequest):
    script = payload.script.strip()
    if not script:
        raise HTTPException(status_code=400, detail="Script is required.")
    try:
        intro_text = await generate_youtube_intro(script)
        if not intro_text:
            raise HTTPException(status_code=500, detail="Failed to generate intro.")
        return IntroResponse(intro=intro_text)
    except Exception as e:
        logger.error("Failed to generate intro", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="An error occurred while generating the intro."
        )