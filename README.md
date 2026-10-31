# Optional backend scaffold

This FastAPI package is currently not connected to the Android application and does not call an AI provider. VEDA's current chat is intended to run locally through LiteRT-LM.

The backend exists only as a starter contract/policy scaffold. Do not deploy it publicly as-is: it has no authentication, rate limiting, or production hardening. It does not execute tools.

## Run tests

```bash
python -m pip install -r requirements.txt
pytest -q
```

## Run locally

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open `/docs` for the scaffold API documentation and `/health` for its health check.
