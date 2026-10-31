from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from .policy import classify_action


app = FastAPI(title="VEDA Assistant API", version="0.1.0")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=8000)
    conversation_id: str | None = None

    @field_validator("message")
    @classmethod
    def message_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("message must not be blank")
        return value.strip()


class ActionPreviewRequest(BaseModel):
    action: str = Field(min_length=1, max_length=120)
    arguments: dict = Field(default_factory=dict)


@app.get('/health')
def health():
    return {"status": "ok", "stage": "scaffold"}


@app.post('/v1/chat')
def chat(request: ChatRequest):
    # Provider integration intentionally not wired yet; no tool execution here.
    return {
        "reply": "VEDA backend scaffold is running. AI provider integration is not configured yet.",
        "conversation_id": request.conversation_id,
        "actions": [],
        "status": "provider_not_configured",
    }


@app.post('/v1/actions/preview')
def action_preview(request: ActionPreviewRequest):
    result = classify_action(request.action)
    return {
        "allowed": result.decision.value != "deny",
        "decision": result.decision.value,
        "requires_approval": result.decision.value == "approval_required",
        "reason": result.reason,
    }
