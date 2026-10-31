# API contract notes

## `POST /v1/chat`
Request: `{ "message": "string", "conversation_id": "optional string" }`
Response: `{ "reply": "string", "actions": [] }`

## `POST /v1/actions/preview`
Request: `{ "action": "string", "arguments": {}, "requires_approval": true }`
Response: `{ "allowed": boolean, "requires_approval": boolean, "reason": "string" }`

The server must never execute device actions. Android owns the UI, permissions, and user-confirmation flow. Unknown action names are denied by default.
