from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.agent_card import load_agent_card
from app.models import ChatRequest, ChatResponse, TranscriptionResponse
from app.services.groq_service import GroqService, GroqServiceError

router = APIRouter()
groq_service = GroqService()


@router.get("/agent-card", tags=["agent"])
def agent_card() -> dict:
    return load_agent_card()


@router.post("/chat", response_model=ChatResponse, tags=["agent"])
def chat(request: ChatRequest) -> ChatResponse:
    try:
        answer = groq_service.chat(request.message, system_prompt=request.system_prompt)
    except GroqServiceError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return ChatResponse(answer=answer)


@router.post("/transcribe", response_model=TranscriptionResponse, tags=["speech"])
async def transcribe(file: UploadFile = File(...)) -> TranscriptionResponse:
    audio_bytes = await file.read()
    if not audio_bytes:
        raise HTTPException(status_code=400, detail="Uploaded audio file is empty.")

    try:
        text = groq_service.transcribe(audio_bytes, filename=file.filename or "audio.wav")
    except GroqServiceError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return TranscriptionResponse(text=text)

