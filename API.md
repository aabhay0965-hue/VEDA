# API scaffold

The optional FastAPI scaffold currently exposes:

- `GET /health` — reports scaffold status.
- `POST /v1/chat` — validates a chat message and returns a placeholder response. It does not invoke a model.
- `POST /v1/actions/preview` — classifies an action name using the deny-by-default policy module. It does not execute the action.

This API is not used by the Android app in the local-model prototype. There is no configured backend URL, API key, or remote inference provider.
