# Vercel Deployment

SpeechTrain is prepared for Vercel's Python runtime as a FastAPI ASGI app.

## Files That Matter

- `app/main.py` exposes the FastAPI `app`.
- `api/index.py` is the Vercel Serverless Function adapter that imports `app.main:app`.
- `pyproject.toml` sets `[tool.vercel] entrypoint = "api.index:app"`.
- `.python-version` pins Vercel/local runtime intent to Python 3.12.
- `vercel.json` includes static assets and `croo-agent.json` in the serverless function bundle.
- `.vercelignore` keeps local-only files out of deployment.

## Environment Variables

Set these in Vercel Project Settings.

Required:

- `GROQ_API_KEY`

Optional:

- `GROQ_TEXT_MODEL`
- `GROQ_TRANSCRIPTION_MODEL`
- `CROO_PRIVATE_KEY`
- `CROO_API_URL`
- `CROO_WS_URL`

## Deploy With Vercel CLI

Install and log in:

```powershell
npm install -g vercel
vercel login
```

Preview deploy:

```powershell
vercel
```

Production deploy:

```powershell
vercel --prod
```

## Post-Deploy Checks

Replace `<deployment-url>` with the Vercel URL.

```powershell
Invoke-RestMethod https://<deployment-url>/health
Invoke-RestMethod https://<deployment-url>/api/v1/agent-card
```

Open the landing/testing page:

```text
https://<deployment-url>/
```

## Notes

The chat and transcription endpoints require `GROQ_API_KEY`. Without it, the API will still deploy and `/health` will work, but Groq-backed requests will return a configuration error.
