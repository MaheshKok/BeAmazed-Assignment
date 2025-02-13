import openai
import logging

from openai import OpenAI, AsyncOpenAI

from config import settings
from aiocache import cached, Cache
import hashlib

logger = logging.getLogger(__name__)

# Configure the OpenAI client with your API key
openai.api_key = settings.OPENAI_API_KEY

client = AsyncOpenAI(
    api_key=openai.api_key,  # This is the default and can be omitted
)

# A custom key builder to ensure the cache key is based on the script content
def key_builder(func, *args, **kwargs):
    # Assume the first argument is the script text
    script = args[0] if args else kwargs.get("script", "")
    return "youtube_intro:" + hashlib.md5(script.encode()).hexdigest()

@cached(ttl=3600, cache=Cache.REDIS, key_builder=key_builder)
async def generate_youtube_intro(script: str) -> str:
    """
    Generates a catchy YouTube intro given a video script.
    Uses the asynchronous acast method from the latest OpenAI Python library.
    """
    prompt = (
        f"Write a catchy YouTube intro for the following video script:\n\n{script}"
    )
    try:
        # Directly await the asynchronous completion call
        response = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
        if response and response.choices:
            return response.choices[0].message.content
        else:
            return ""
    except Exception as e:
        logger.error("Error calling OpenAI API", exc_info=True)
        raise e