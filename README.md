# SpeechTrain

SpeechTrain is an AI agent that coaches people on how to hold better conversations. It helps users start and finish conversations, choose what to say next, ask stronger follow-up questions, and keep a conversation partner curious and involved in both casual and professional settings.

It uses FastAPI for the HTTP API and Groq for low-latency coaching and speech transcription calls.

## Setup

Install Python 3.11 or newer, then create the virtual environment in this project:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Create a local environment file:

```powershell
Copy-Item .env.example .env
```

Set `GROQ_API_KEY` in `.env`, then run the API:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open:

- Landing and test page: `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## API Surface

- `GET /health` reports service status and configured models.
- `POST /api/v1/chat` sends a conversation-coaching prompt to Groq.
- `POST /api/v1/transcribe` accepts an uploaded practice conversation or voice note and returns transcription text.
- `GET /api/v1/agent-card` exposes listing metadata from `croo-agent.json`.

## Croo Store Preparation

`croo-agent.json` is a listing-ready manifest based on common agent marketplace metadata patterns. Public research did not find an official Croo Agent Network Store submission schema, so confirm the required format before submission.

Croo's public developer path at `croo.network` points to the CAP SDK and service registration flow. This project includes `CROO_PRIVATE_KEY`, `CROO_API_URL`, and `CROO_WS_URL` placeholders so the agent can be adapted into a Croo provider once you have wallet and submission details.

## Vercel Deployment

This project is prepared for Vercel's Python runtime with `app.main:app` as the ASGI entrypoint.

Required Vercel environment variable:

- `GROQ_API_KEY`

Optional Vercel environment variables:

- `GROQ_TEXT_MODEL`
- `GROQ_TRANSCRIPTION_MODEL`
- `CROO_PRIVATE_KEY`
- `CROO_API_URL`
- `CROO_WS_URL`

See `docs/deployment.md` for deployment steps.

## Checks

```powershell
pytest
ruff check .
```
