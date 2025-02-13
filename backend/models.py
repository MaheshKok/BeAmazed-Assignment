from pydantic import BaseModel, Field

class ScriptRequest(BaseModel):
    script: str = Field(
        ...,
        min_length=10,
        example="Describe the wonders of space exploration."
    )

class IntroResponse(BaseModel):
    intro: str