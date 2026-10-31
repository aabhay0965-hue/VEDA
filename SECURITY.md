# VEDA security model (prototype)

## Current boundary

The current Android prototype is a local chat/model loader. It does not perform phone actions, read notifications, send messages, make payments, or connect to an AI API. No broad permissions are intentionally requested by the manifest.

The optional FastAPI backend is a scaffold. `backend/app/policy.py` classifies a small set of proposed action names; it does not execute them, authenticate users, or enforce Android permissions. Do not expose it as a public production service.

## Planned action safety requirements

Before adding device actions, implement all of the following in code:

- A fixed registry of named tools; no model-generated arbitrary function, URL scheme, command, or code execution.
- Strict schemas and bounded arguments for every tool.
- Deny-by-default classification and separate Android-side checks.
- Permission checks at the point of use; Android remains the authority for runtime permissions.
- Explicit approval for sending messages, creating/updating/deleting calendar events, publishing, sharing, or transmitting personal data.
- Approval UI that shows exact recipient, content, and action; approval must be one-time and bound to the exact proposed action.
- Cancellation, timeout, and rejection paths that do not execute the action.
- No payments, credential access, shell/root, silent installs, security bypasses, unrestricted accessibility automation, or policy self-modification.
- No sensitive prompt/notification contents in logs by default.

## Data and model

- The selected model is imported through Android's document picker and copied to app-private storage.
- The model file is not included in source control or the APK.
- Chat is intended to remain on-device. Verify dependency/runtime behavior before claiming the app is fully offline.
- Do not commit `.env`, keys, tokens, signing keys, user data, or private model files.

## Reporting

This is not a security-audited application. Do not use it for sensitive or consequential tasks. Report issues privately to the repository owner before publishing details.
