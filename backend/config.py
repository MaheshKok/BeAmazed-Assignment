import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_ENGINE: str = os.getenv("OPENAI_ENGINE", "text-davinci-003")
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", 100))
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", 0.7))

settings = Settings()

if not settings.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")