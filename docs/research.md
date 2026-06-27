# SpeechTrain Research Notes

Research date: 2026-06-27

## Goal

Scaffold a local AI agent named SpeechTrain with:

- A Python virtual environment path inside the project.
- FastAPI for the API server.
- Groq for chat and speech transcription.
- A listing-ready metadata file for the Croo Agent Network Store.
- A product direction focused on coaching people through casual and professional conversations.

## Findings

### FastAPI

FastAPI remains a strong fit for this scaffold because it provides:

- Automatic OpenAPI documentation at `/docs`.
- Pydantic-based request and response validation.
- Native async support for upload endpoints.
- A simple APIRouter pattern for keeping endpoints modular.

Relevant official docs:

- First steps and app creation: https://fastapi.tiangolo.com/tutorial/first-steps/
- Bigger applications and routers: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- File uploads: https://fastapi.tiangolo.com/tutorial/request-files/

Implementation decision:

- `app/main.py` creates the FastAPI app.
- `app/api/routes.py` owns the agent routes.
- `app/models.py` owns request and response schemas.

### Groq

Groq provides an official Python SDK and OpenAI-style chat completion APIs. Its docs also cover audio transcription models, including Whisper-family models.

Relevant official docs:

- Groq quickstart: https://console.groq.com/docs/quickstart
- Groq text chat: https://console.groq.com/docs/text-chat
- Groq speech-to-text: https://console.groq.com/docs/speech-to-text
- Groq models: https://console.groq.com/docs/models

Implementation decision:

- `app/services/groq_service.py` wraps Groq calls behind a small service class.
- `GROQ_API_KEY` is read from `.env`.
- Default text model: `llama-3.3-70b-versatile`.
- Default transcription model: `whisper-large-v3-turbo`.
- The default system prompt defines SpeechTrain as a conversation coach, not a general presentation coach.

### SpeechTrain Agent Scope

SpeechTrain is focused on conversation skill-building. The agent should help users:

- Start conversations without sounding stiff or generic.
- Continue conversations with curious follow-up questions.
- Balance talking and listening.
- Transition between topics naturally.
- Adapt tone for casual, social, workplace, sales, interview, or networking contexts.
- End conversations warmly without making the exit awkward.
- Review transcripts of practice conversations and suggest better wording.

The default response style should be practical and immediately usable. Strong answers should include sample lines the user can say out loud, plus a short reason why those lines work.

### Croo Agent Network Store

Follow-up research was performed directly against `croo.network`. The public Croo site presents Croo as an agent commerce network and points developers toward the CAP SDK and a registration/provider workflow rather than a simple static app-store upload.

Public Croo pages reviewed:

- Main site: https://croo.network/
- Agent network entry point: https://agent.croo.network/
- CAP developer page: https://cap.croo.network/

Key findings from the public Croo material:

- Croo positions agents as commercial services that can be discovered and purchased through the network.
- The public developer path points to installing a Croo/CAP SDK and shows JavaScript/Node-style setup in the public CAP material reviewed.
- Provider setup appears to require wallet credentials, especially a private key.
- Service registration is part of the network flow.
- A provider process listens for incoming requests, commonly described around WebSocket/network events.

What was not found publicly:

- A formal Croo Agent Network Store submission guide.
- A JSON manifest schema for store listing validation.
- A public validation command or endpoint for pre-submission checks.
- A required screenshot/icon/privacy-policy package format.

Additional searches included combinations of:

- `Croo agent network store`
- `Croo agent marketplace`
- `Croo AI agent network`
- `Croo agents store manifest`
- `site:croo.network Croo CAP service registration`
- `site:croo.network Croo provider private key`

Because no official public store schema was found, this project includes `croo-agent.json` as a draft listing manifest based on common marketplace fields:

- Identity: name, slug, version, tagline, description.
- Discovery: categories and capabilities.
- Runtime: framework, language, Python version.
- API contract: health, agent card, chat, and transcription endpoints.
- Environment: required and optional variables.
- Privacy notes: whether audio or text is persisted.
- Publisher metadata and submission notes.

Action needed before store submission:

1. Get the official Croo Agent Network Store or CAP provider submission requirements.
2. Validate required fields, naming conventions, authentication requirements, endpoint expectations, and wallet requirements.
3. Replace placeholder publisher, repository, contact, and license values.
4. Add store-required screenshots, icons, terms, privacy policy, or verification metadata if Croo requires them.
5. If Croo requires CAP-native registration, implement a provider runner using the public CAP SDK and map incoming CAP requests to the existing FastAPI/Groq service logic.

## Virtual Environment Status

The project is prepared for a `.venv` virtual environment inside the SpeechTrain directory. On this machine, `python`, `py`, and a usable `python3` command were not available during setup. The detected `python3.exe` appears to be the Microsoft Store alias, not an installed interpreter.

After installing Python 3.11 or newer, run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

## Recommended Next Steps

1. Install Python 3.11+ and create `.venv`.
2. Copy `.env.example` to `.env`.
3. Add a Groq API key.
4. Run `uvicorn app.main:app --reload`.
5. Open `http://127.0.0.1:8000/` and use the landing/testing page.
6. Verify `GET /health` and `GET /api/v1/agent-card`.
7. Confirm official Croo listing requirements and update `croo-agent.json`.
