from groq import Groq

from app.core.config import settings


DEFAULT_SYSTEM_PROMPT = (
    "You are SpeechTrain, a practical conversation coaching agent. Help users start, hold, "
    "and finish casual or professional conversations. Coach them on what to say, what to ask, "
    "how to keep the other person curious and involved, when to listen, how to transition, "
    "and how to close warmly. Give concise, specific, ready-to-use wording."
)


class GroqServiceError(RuntimeError):
    """Raised when Groq calls fail or the API key is missing."""


class GroqService:
    def __init__(self) -> None:
        self._client = Groq(api_key=settings.groq_api_key) if settings.groq_api_key else None

    def _require_client(self) -> Groq:
        if self._client is None:
            raise GroqServiceError("GROQ_API_KEY is not configured.")
        return self._client

    def chat(self, message: str, system_prompt: str | None = None) -> str:
        client = self._require_client()
        try:
            completion = client.chat.completions.create(
                model=settings.groq_text_model,
                messages=[
                    {"role": "system", "content": system_prompt or DEFAULT_SYSTEM_PROMPT},
                    {"role": "user", "content": message},
                ],
            )
        except Exception as exc:  # Groq SDK exceptions vary by transport and response type.
            raise GroqServiceError(f"Groq chat request failed: {exc}") from exc

        content = completion.choices[0].message.content
        return content or ""

    def transcribe(self, audio_bytes: bytes, filename: str) -> str:
        client = self._require_client()
        try:
            transcription = client.audio.transcriptions.create(
                file=(filename, audio_bytes),
                model=settings.groq_transcription_model,
            )
        except Exception as exc:
            raise GroqServiceError(f"Groq transcription request failed: {exc}") from exc

        return transcription.text
