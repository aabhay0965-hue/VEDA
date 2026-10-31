from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_returns_typed_reply_and_preserves_conversation_id():
    response = client.post(
        "/v1/chat",
        json={"message": "Hello VEDA", "conversation_id": "conversation-123"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["reply"]
    assert body["conversation_id"] == "conversation-123"
    assert body["actions"] == []
    assert body["status"] == "provider_not_configured"


def test_chat_rejects_blank_message():
    response = client.post("/v1/chat", json={"message": "   "})

    assert response.status_code == 422


def test_chat_rejects_message_over_limit():
    response = client.post("/v1/chat", json={"message": "x" * 8001})

    assert response.status_code == 422
