from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router as api_router
from app.core.config import settings

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATIC_ROOT = PROJECT_ROOT / "static"


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="SpeechTrain AI agent API for conversation coaching workflows.",
        version="0.1.0",
    )
    app.mount("/static", StaticFiles(directory=STATIC_ROOT), name="static")
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/", include_in_schema=False)
    def landing_page() -> FileResponse:
        return FileResponse(STATIC_ROOT / "index.html")

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "app": settings.app_name,
            "environment": settings.app_env,
            "text_model": settings.groq_text_model,
            "transcription_model": settings.groq_transcription_model,
            "croo_api_url": settings.croo_api_url,
            "croo_ws_url": settings.croo_ws_url,
        }

    return app


app = create_app()
