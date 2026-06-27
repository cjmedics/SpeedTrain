from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message or coaching request.")
    system_prompt: str | None = Field(
        default=None,
        description="Optional custom system prompt for a specific speech-training flow.",
    )


class ChatResponse(BaseModel):
    answer: str


class TranscriptionResponse(BaseModel):
    text: str

